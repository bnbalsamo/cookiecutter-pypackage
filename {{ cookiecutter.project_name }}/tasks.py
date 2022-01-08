"""Development tasks for {{ cookiecutter.project_name }}."""
import os
import sys
from pathlib import Path
from shlex import quote
from shutil import rmtree
from tempfile import TemporaryDirectory
from typing import Callable, Iterable, Tuple

from invoke import Collection, task

# Change the CWD to the repo root.
os.chdir(Path(__file__).parent.resolve())


# Differentiate our output from called app output.
ECHO_PREFIX = "=> "


def echo(msg):
    """Wrap print to prepend a prefix."""
    print(ECHO_PREFIX + str(msg))


echo(f"Current Working Directory: {str(Path('.').resolve())}")


def get_posargs():
    """Get tox style "posargs" that follow "--" on the CLI."""
    try:
        return sys.argv[sys.argv.index("--") + 1 :]
    except (ValueError, IndexError):
        return []


def run_argv(ctx, argv, warn=False):
    """Run a constructed argv via the provided context."""
    return ctx.run(" ".join([quote(x) for x in argv]), warn=warn)


@task
def lint(ctx):
    """Run pre-commit against all files."""
    argv = [
        "poetry",
        "run",
        "pre-commit",
        "run",
        "--all-files",
        "--show-diff-on-failure",
    ]
    run_argv(ctx, argv, warn=False)


@task(name="format")
def format_(ctx):
    """Run all the formatters."""
    for formatter in (
        "black",
        "blacken-docs",
        "isort",
        "end-of-file-fixer",
        "trailing-whitespace",
    ):
        argv = (
            "poetry",
            "run",
            "pre-commit",
            "run",
            "--all-files",
            "--show-diff-on-failure",
            formatter,
        )
        run_argv(ctx, argv, warn=True)


@task(pre=[format_])
def test(ctx):
    """Run the tests."""
    clean_coverage()
    argv = ["poetry", "run", "nox"]
    argv.extend(get_posargs())
    run_argv(ctx, argv)


@task(name="docs")
def build_docs(ctx, clean_=True, buildername="html"):
    """Build the documentation."""
    if clean_:
        clean_docs()
    argv = [
        "poetry",
        "run",
        "sphinx-build",
        "docs",
        "docs_out",
        "--color",
        "-W",
        f"-b{buildername}",
    ]
    run_argv(ctx, argv)
    docs_dir = Path(".") / "docs_out"
    docs_dir = docs_dir.resolve()
    echo(f"Docs available in {str(docs_dir)}")


def remove_directory(directory, raise_=False):
    """
    Remove a directory.

    If raise_ is True and the directory doesn't exist raise an exception.
    """
    if not directory.exists():
        if raise_:
            raise FileNotFoundError(directory)
        echo(f"No directory found at {str(directory)}")
        return
    rmtree(directory)
    echo(f"{str(directory)} removed.")


def clean_dists():
    """Remove existing distributions."""
    dist_dir = Path("./dist").resolve()
    remove_directory(dist_dir)


def clean_docs():
    """Remove existing docs."""
    docs_out_dir = Path("./docs_out").resolve()
    remove_directory(docs_out_dir)


def clean_compiled(dir_=None, _recursing=False):
    """Remove compiled python artifacts from a directory recursively."""
    if dir_ is None:
        dir_ = Path().resolve()  # cwd

    # Names to skip removing or recursing into
    bad_names = [
        "venv",
        ".venv",
        "env",
        ".env",
        ".git",
    ]

    if not _recursing:
        echo(f"Removing compiled artifacts from {str(dir_)} recursively...")
    for entry in dir_.iterdir():
        if entry.name in bad_names:
            continue
        if entry.name.endswith(".pyc"):
            entry.unlink()
            continue
        if entry.name == "__pycache__" or entry.name.endswith(".egg-info"):
            rmtree(entry)
            continue
        if entry.is_dir():
            clean_compiled(dir_=entry, _recursing=True)


def clean_nox():
    """Remove the .nox cache directory."""
    nox_dir = Path("./.nox").resolve()
    remove_directory(nox_dir)


def clean_mypy():
    """Remove the .mypy_cache directory."""
    mypy_cache_dir = Path("./.mypy_cache").resolve()
    remove_directory(mypy_cache_dir)


def clean_coverage():
    """Remove the .coverage cache."""
    # Nox takes care of .coverage on its own
    # We just don't want extras in our coverage combine call.
    for coverage_cache_file in Path().glob(".coverage.*"):
        if coverage_cache_file.exists() and coverage_cache_file.is_file():
            coverage_cache_file.unlink()
            echo(f"{str(coverage_cache_file)} removed.")


def clean_coverage_report():
    """Remove the html coverage report."""
    coverage_report_dir = Path("./htmlcov").resolve()
    remove_directory(coverage_report_dir)


def clean_build_dir():
    """Remove the build directory."""
    build_directory = Path("./build").resolve()
    remove_directory(build_directory)


def clean_pytest():
    """Remove the pytest cache directory."""
    pytest_cache_directory = Path("./.pytest_cache").resolve()
    remove_directory(pytest_cache_directory)


@task
def clean(
    ctx,
    dists=True,
    docs=True,
    compiled=True,
    nox=True,
    mypy=True,
    pytest=True,
    coverage=True,
    coverage_report=True,
    build_directory=True,
):  # pylint:disable=W0613,R0913
    """
    Clean up all caches and generated artifacts.

    Note that the default is to clean _everything_, and if you would like to
    preserve any artifacts/caches you should pass the corresponding `--no-...`
    flag to this command.
    """
    cleaners: Iterable[Tuple[bool, Callable]] = (
        (dists, clean_dists),
        (docs, clean_docs),
        (compiled, clean_compiled),
        (nox, clean_nox),
        (mypy, clean_mypy),
        (pytest, clean_pytest),
        (coverage, clean_coverage),
        (coverage_report, clean_coverage_report),
        (build_directory, clean_build_dir),
    )
    for entry in cleaners:
        if entry[0]:  # If the arg is true
            entry[1]()  # Run the cleaner


@task(name="dists")
def build_dists(ctx):
    """Build distribution artifacts."""
    clean_dists()
    clean_build_dir()
    argv = ["poetry", "run", "python", "-m", "build", "."]
    run_argv(ctx, argv)
    echo(f"Dists now available in {Path('./dist').resolve()}")


@task(name="zipapp")
def build_zipapp(
    ctx,
    command_name=None,
    executable_name=None,
    shebang=None,
    compress=False,
):  # pylint:disable=R0913
    """Use `shiv` to produce a zipapp that includes the dependencies."""
    # Defaults
    if shebang is None:
        shebang = "/usr/bin/env python3"

    if executable_name is None:
        if command_name is not None:
            # Same name as command
            executable_name = command_name
        else:
            # Same name as project directory
            executable_name = Path().resolve().name

    # Compute output path
    dist_dir = Path() / "dist"
    dist_dir.mkdir(exist_ok=True)
    output_fname = dist_dir / executable_name

    echo("Creating zipapp with shiv")
    with TemporaryDirectory() as tmp_dir:
        # Build a requirements.txt
        reqs_filepath = Path(tmp_dir) / "requirements.txt"
        echo(f"Creating requirements.txt at {str(reqs_filepath.resolve())}")
        run_argv(
            ctx,
            [
                "poetry",
                "export",
                "--format=requirements.txt",
                f"--output={str(reqs_filepath.resolve())}",
            ],
        )

        # Build a site-packages dir
        echo(f"Creating temporary site_packages at {tmp_dir}/site-packages")
        run_argv(
            ctx,
            [
                "python",
                "-m",
                "pip",
                "install",
                "--no-deps",
                "-r",
                f"{str(reqs_filepath.resolve())}",
                "--target",
                f"{tmp_dir}/site-packages",
            ],
        )
        ctx.run(f"python -m pip install . --target {tmp_dir}/site-packages")

        # Build the shiv argv
        shiv_cmd = [
            "poetry",
            "run",
            "shiv",
            "--site-packages",
            f"{tmp_dir}/site-packages",
            "-p",
            shebang,
            "-o",
            str(output_fname),
        ]

        if command_name:
            shiv_cmd.extend(["-c", command_name])
        if compress:
            shiv_cmd.append("--compressed")
        # Run the shiv command
        run_argv(ctx, shiv_cmd)
    echo(f"Created zipapp: {output_fname}")


@task(pre=[test], name="coverage-report")
def build_coverage_report(ctx):
    """Build an HTML coverage report."""
    run_argv(ctx, ["poetry", "run", "coverage", "html"])
    echo(f"Coverage report available at {str(Path('./htmlcov').resolve())}")


@task(name="todos")
def check_todos(ctx):
    """Check for `#TODO` comments in the code."""
    argv = [
        "poetry",
        "run",
        "pylint",
        "--disable=all",
        "--enable=W0511",
        "src",
        "tests",
    ]
    run_argv(ctx, argv)


@task(pre=[test, lint, build_dists])
def release(ctx, prod=False):
    """Perform a release to pypi."""
    argv = ["python", "-m", "twine", "upload"]
    if not prod:
        echo("Uploading to test.pypi")
        argv.extend(["--repository-url", "https://test.pypi.org/legacy"])
    else:
        echo("--prod flag present. Uploading to pypi")
    argv.append("./dist/*")
    run_argv(ctx, argv)
    echo("Upload complete")


@task(name="docs", iterable=["additional_dir"])
def serve_docs(ctx, todos=False, additional_dir=None, open_browser=False):
    """Serve the docs on localhost:8000. Reload on changes."""
    argv = ["poetry", "run", "sphinx-autobuild"]

    if open_browser:
        argv.append("--open-browser")

    # Default additional dirs we want to watch for changes
    default_additional_dirs = ["src"]
    for default in default_additional_dirs:
        additional_dir.append(default)

    # Append append defaults + user specified dirs to argv
    additional_dir.append("src")
    for dir_ in additional_dir:
        argv.append("--watch")
        argv.append(dir_)

    # sphinx-autobuild positional args
    argv.append("docs")
    argv.append("docs/_build/html")

    # See relevant logic in docs/conf.py
    if todos:
        os.environ["SPHINX_DISPLAY_TODOS"] = "true"

    run_argv(ctx, argv)


# Make implicit root explicit
ns = Collection()
# Apply some default configurations
ns.configure({"run": {"pty": True, "echo": True}})


# Root commands
ns.add_task(release)
ns.add_task(clean)
ns.add_task(format_)
ns.add_task(test)
ns.add_task(lint)


# Define the "build" subcommand
build_ns = Collection("build")
build_ns.add_task(build_dists, default=True)
build_ns.add_task(build_docs)
build_ns.add_task(build_coverage_report)
build_ns.add_task(build_zipapp)


# Define the "check" subcommand
check_ns = Collection("check")
check_ns.add_task(check_todos)


# Define the "serve" subcommand
serve_ns = Collection("serve")
serve_ns.add_task(serve_docs)


# Add custom subcommands to root namespace
ns.add_collection(build_ns)
ns.add_collection(check_ns)
ns.add_collection(serve_ns)
