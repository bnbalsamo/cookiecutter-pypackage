"""Development tasks for {{ cookiecutter.project_name }}."""
import os
from glob import glob
from pathlib import Path
from shlex import quote
from shutil import rmtree
from tempfile import TemporaryDirectory

from invoke import Collection, task

# Change the CWD to the repo root.
_LAST_DIR = None
while not Path("./tasks.py").exists():
    os.chdir("..")
    _CURRENT_DIR = Path(".").resolve()
    if _CURRENT_DIR == _LAST_DIR:
        # We hit the FS root :(
        raise FileNotFoundError("Could not find the repository root.")


# Differentiate our output from called app output.
ECHO_PREFIX = "=> "


def echo(msg):
    """Wrap print to prepend a prefix."""
    print(ECHO_PREFIX + str(msg))


@task(name="pindeps")
def pindeps(ctx, generate_hashes=True, upgrade=True):
    """Pin dependencies."""
    argv = ["python", "-m", "piptools", "compile"]
    if generate_hashes:
        argv.append("--generate-hashes")
    if upgrade:
        argv.append("-U")
    os.environ["CUSTOM_COMPILE_COMMAND"] = "inv[oke] pindeps"
    argv.append("setup.cfg")
    ctx.run(" ".join([quote(x) for x in argv]))
    req_path = Path(".") / "requirements.txt"
    req_path = req_path.resolve()
    echo(f"Dependencies pinned in {str(req_path)}")


@task(name="black")
def run_black(ctx, warn=False):
    """Run `black` to autoformat the source code."""
    # The result of this command should satisfy the
    # corresponding tox testenv check_black
    ctx.run("python -m black ./src ./tests setup.py tasks.py", warn=warn)


@task(name="blacken_docs")
def run_blacken_docs(ctx, warn=False):
    """Run `blacken-docs` to autoformat code in the documentation."""
    # The result of this command should satisfy the
    # corresponding tox testenv check_blacken_docs
    docs_paths = ["README.md"]
    docs_paths += glob("docs/**/*.rst", recursive=True)
    docs_paths += glob("src/**/*.py", recursive=True)
    docs_paths = [quote(p) for p in docs_paths]
    ctx.run("blacken-docs %s" % " ".join(docs_paths), warn=warn)


@task(name="isort")
def run_isort(ctx, warn=False):
    """Run `isort` to autoformat the source code."""
    # The result of this command should satisfy the
    # corresponding tox testenv check_isort
    ctx.run("python -m isort ./src ./tests tasks.py setup.py", warn=warn)


@task(name="autoformatters")
def run_autoformatters(ctx, warn=False):
    """Run all the autoformatters."""
    run_black(ctx, warn=warn)
    run_blacken_docs(ctx, warn=warn)
    run_isort(ctx, warn=warn)


@task(name="tests", iterable=["env"])
def run_tests(ctx, autoformat=True, warn=False, env=None, recreate=False):
    """Run the tests."""
    if autoformat:
        run_autoformatters(ctx, warn=warn)
    argv = ["tox"]
    if env:
        argv.append("-e")
        argv.append(",".join(env))
    if recreate:
        argv.append("--recreate")
    ctx.run(" ".join([quote(x) for x in argv]), warn=warn)


@task(name="docs")
def build_docs(ctx, clean=True, buildername="html"):
    """Build the documentation."""
    if clean:
        clean_docs(ctx)
    ctx.run(f"sphinx-build docs docs_out --color -W -b{buildername}")
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


@task(name="dists")
def clean_dists(ctx):  # pylint:disable=W0613
    """Remove existing distributions."""
    dist_dir = Path("./dist").resolve()
    remove_directory(dist_dir)


@task(name="docs")
def clean_docs(ctx):  # pylint:disable=W0613
    """Remove existing docs."""
    docs_out_dir = Path("./docs_out").resolve()
    remove_directory(docs_out_dir)


@task(name="compiled")
def clean_compiled(ctx):  # pylint:disable=W0613
    """Remove compilation artifacts."""

    def clean_dir(dir_):
        """Remove compiled python artifacts from a directory."""
        for entry in dir_.iterdir():
            if entry.name.endswith(".pyc"):
                entry.unlink()
                continue
            if entry.name == "__pycache__" or entry.name.endswith(".egg-info"):
                rmtree(entry)
                continue
            if entry.is_dir():
                clean_dir(entry)

    dirs_to_clean = [
        Path("./src").resolve(),
        Path("./tests").resolve(),
    ]
    for dir_ in dirs_to_clean:
        echo(f"Removing compiled/cache artifacts in {str(dir_)}")
        clean_dir(dir_)
    echo("Compiled artifacts and caches removed")


@task(name="tox")
def clean_tox(ctx):  # pylint:disable=W0613
    """Remove the .tox cache directory."""
    tox_dir = Path("./.tox").resolve()
    remove_directory(tox_dir)


@task(name="mypy")
def clean_mypy(ctx):  # pylint:disable=W0613
    """Remove the .mypy_cache directory."""
    mypy_cache_dir = Path("./.mypy_cache").resolve()
    remove_directory(mypy_cache_dir)


@task(name="coverage")
def clean_coverage(ctx):  # pylint:disable=W0613
    """Remove the .coverage cache."""
    coverage_cache_file = Path("./.coverage").resolve()
    if coverage_cache_file.exists() and coverage_cache_file.is_file():
        coverage_cache_file.unlink()
        echo(f"{str(coverage_cache_file)} removed.")
    else:
        echo(f"No file found at {str(coverage_cache_file)}")


@task(name="wheelhouse")
def clean_wheelhouse(ctx):  # pylint:disable=W0613
    """Remove the wheelhouse."""
    wheelhouse_dir = Path("./wheelhouse").resolve()
    remove_directory(wheelhouse_dir)


@task(name="coverage-report")
def clean_coverage_report(ctx):  # pylint:disable=W0613
    """Remove the html coverage report."""
    coverage_report_dir = Path("./htmlcov").resolve()
    remove_directory(coverage_report_dir)


@task(name="build-dir")
def clean_build_dir(ctx):  # pylint:disable=W0613
    """Remove the build directory."""
    build_directory = Path("./build").resolve()
    remove_directory(build_directory)


@task(name="all")
def clean_all(
    ctx,
    dists=True,
    docs=True,
    compiled=True,
    tox=True,
    mypy=True,
    coverage=True,
    wheelhouse=True,
    coverage_report=True,
    build_directory=True,
):  # pylint:disable=R0913
    """Remove all clean-able artifacts."""
    if dists:
        clean_dists(ctx)
    if docs:
        clean_docs(ctx)
    if compiled:
        clean_compiled(ctx)
    if tox:
        clean_tox(ctx)
    if mypy:
        clean_mypy(ctx)
    if coverage:
        clean_coverage(ctx)
    if wheelhouse:
        clean_wheelhouse(ctx)
    if coverage_report:
        clean_coverage_report(ctx)
    if build_directory:
        clean_build_dir(ctx)


@task(name="dists")
def build_dists(ctx, clean=True):
    """Build distribution artifacts."""
    if clean:
        clean_dists(ctx)
        clean_build_dir(ctx)
    ctx.run("python -m build -s -w .")
    echo(f"Dists now available in {Path('./dist').resolve()}")


@task(name="zipapp")
def build_zipapp(
    ctx,
    command_name=None,
    executable_name=None,
    pin_dependencies=True,
    shebang=None,
    compress=False,
):  # pylint:disable=R0913
    """Use `shiv` to produce a zipapp that includes the depndencies."""
    if pin_dependencies:
        pindeps(ctx)

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

    # Run shiv
    echo("Creating zipapp with shiv")
    with TemporaryDirectory() as tmp_dir:
        # Build the shiv argv
        shiv_cmd = [
            "shiv",
            "--site-packages",
            tmp_dir,
            "-p",
            shebang,
            "-o",
            str(output_fname),
        ]

        if command_name:
            shiv_cmd.extend(["-c", command_name])
        if compress:
            shiv_cmd.append("--compressed")
        echo(f"Creating temporary site_packages at {tmp_dir}")
        # pip-sync doesn't appear to suport the `--target` option :(
        # https://github.com/jazzband/pip-tools/issues/587
        # Should be okay, as there aren't going to be any extra
        # packages in the purpose build site-packages anyways.
        ctx.run(f"python -m pip install -r requirements.txt --target {tmp_dir}")
        ctx.run(f"python -m pip install . --target {tmp_dir}")
        ctx.run(" ".join([quote(x) for x in shiv_cmd]))
    echo(f"Created zipapp: {output_fname}")


@task(name="wheelhouse")
def build_wheelhouse(ctx, clean=True, pin_dependencies=True):
    """Build a dependency wheelhouse."""
    if clean:
        clean_wheelhouse(ctx)
    if pin_dependencies:
        pindeps(ctx)
    ctx.run("python -m pip wheel -w wheelhouse -r requirements.txt")
    echo(f"Wheelhouse now available in {Path('./wheelhouse').resolve()}")


@task(name="coverage-report")
def build_coverage_report(ctx, clean=True, test=True):
    """Build an HTML coverage report."""
    if clean:
        clean_coverage_report(ctx)
    if test:
        run_tests(ctx, warn=True)
    ctx.run("coverage html")
    echo(f"Coverage report available at {str(Path('./htmlcov').resolve())}")


@task(name="todos")
def check_todos(ctx):
    """Check for `#TODO` comments in the code."""
    ctx.run("python -m pylint --disable=all --enable=W0511 src tests")


@task()
def release(
    ctx, prod=False, clean=True, build=True, skip_tests=False, autoformat=True
):  # pylint:disable=R0913
    """Perform a release to pypi."""
    if not skip_tests:
        run_tests(ctx, autoformat=autoformat)
    if clean:
        clean_dists(ctx)
    if build:
        build_dists(ctx)
    cmd = "python -m twine upload"
    if not prod:
        echo("Uploading to test.pypi")
        cmd += " --repository-url https://test.pypi.org/legacy"
    else:
        echo("--prod flag present. Uploading to pypi")
    cmd += " ./dist/*"
    ctx.run(cmd)
    echo("Upload complete")


@task(name="docs", iterable=["additional_dir"])
def serve_docs(ctx, todos=False, additional_dir=None, open_browser=False):
    """Serve the docs on localhost:8000. Reload on changes."""
    argv = ["sphinx-autobuild"]

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

    ctx.run(" ".join([quote(x) for x in argv]))


# Make implicit root explicit
ns = Collection()
# Apply some default configurations
ns.configure({"run": {"pty": True, "echo": True}})


# Root commands
ns.add_task(pindeps)
ns.add_task(release)


# Define the "run" subcommand
run_ns = Collection("run")
run_ns.add_task(run_autoformatters)
run_ns.add_task(run_black)
run_ns.add_task(run_blacken_docs)
run_ns.add_task(run_isort)
run_ns.add_task(run_tests)


# Define the "build" subcommand
build_ns = Collection("build")
build_ns.add_task(build_dists, default=True)
build_ns.add_task(build_docs)
build_ns.add_task(build_wheelhouse)
build_ns.add_task(build_coverage_report)
build_ns.add_task(build_zipapp)


# Define the "clean" subcommand
clean_ns = Collection("clean")
clean_ns.add_task(clean_all, default=True)
clean_ns.add_task(clean_dists)
clean_ns.add_task(clean_docs)
clean_ns.add_task(clean_compiled)
clean_ns.add_task(clean_tox)
clean_ns.add_task(clean_mypy)
clean_ns.add_task(clean_coverage)
clean_ns.add_task(clean_wheelhouse)
clean_ns.add_task(clean_coverage_report)


# Define the "check" subcommand
check_ns = Collection("check")
check_ns.add_task(check_todos)


# Define the "serve" subcommand
serve_ns = Collection("serve")
serve_ns.add_task(serve_docs)


# Add custom subcommands to root namespace
ns.add_collection(run_ns)
ns.add_collection(build_ns)
ns.add_collection(clean_ns)
ns.add_collection(check_ns)
ns.add_collection(serve_ns)
