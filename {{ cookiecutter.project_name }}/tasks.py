"""
Development tasks for {{ cookiecutter.project_name }}
"""
import os
from pathlib import Path
from shutil import rmtree

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
    # Wrap print to append a prefix
    print(ECHO_PREFIX + str(msg))


@task(name="pindeps")
def _pindeps(c):
    """
    Pin dependencies, creating or overwriting requirements.txt
    """
    # Requires being run in a fresh virtualenv,
    # so we leverage tox
    echo("Pinning dependencies...")
    c.run("tox -e pindeps --recreate")
    # This must be in sync with tox.ini
    req_path = Path(".") / "requirements.txt"
    req_path = req_path.resolve()
    echo(f"Dependencies pinned in {str(req_path)}")


@task(name="black")
def run_black(c):
    """
    Run `black` to autoformat the source code.
    """
    # The result of this command should satisfy the
    # corresponding tox testenv check_black
    echo("Running black...")
    c.run("python -m black ./src ./tests")
    echo("Blackening complete")


@task(name="isort")
def run_isort(c):
    """
    Run `isort` to autoformat the source code.
    """
    # The result of this command should satisfy the
    # corresponding tox testenv check_isort
    echo("Running isort...")
    c.run("python -m isort ./src ./tests")
    echo("Isort-ing complete")


@task(name="autoformatters")
def run_autoformatters(c):
    """
    Run all the autoformatters.
    """
    echo("Running all autoformatters...")
    run_black(c)
    run_isort(c)
    echo("Autoformatting complete")


@task(name="tests")
def run_tests(c, autoformat=False, tox_args=None):
    """
    Run the tests.
    """
    echo("Running tests...")
    if autoformat:
        run_autoformatters(c)
    cmd = "tox"
    if tox_args:
        cmd = cmd + " %s" % tox_args
    c.run(cmd)
    echo("Testing complete")


@task(name="docs")
def build_docs(c, clean=True, buildername="html"):
    """
    Build the documentation.
    """
    echo("Building docs...")
    if clean:
        clean_docs(c)
    c.run(f"sphinx-build docs docs_out --color -W -b{buildername}")
    docs_dir = Path(".") / "docs_out"
    docs_dir = docs_dir.resolve()
    echo(f"Docs available in {str(docs_dir)}")


@task(name="dists")
def clean_dists(c):
    """
    Remove existing distributions.
    """
    dist_dir = Path("./dist").resolve()
    if not dist_dir.exists():
        echo(f"No dist dir found at {str(dist_dir)}")
        return
    if not dist_dir.is_dir():
        raise NotADirectoryError(dist_dir)
    echo(f"Removing existing dist dir: {str(dist_dir)}...")
    for contents in dist_dir.iterdir():
        contents.unlink()
    dist_dir.rmdir()
    echo("Dist dir removed")


@task(name="docs")
def clean_docs(c):
    """
    Remove existing docs.
    """
    docs_out_dir = Path("./docs_out").resolve()
    if not docs_out_dir.exists():
        echo(f"No rendered docs dir found at {str(docs_out_dir)}")
        return
    if not docs_out_dir.is_dir():
        raise NotADirectoryError(docs_out_dir)
    echo(f"Removing existing rendered docs dir: {str(docs_out_dir)}...")
    rmtree(docs_out_dir)
    echo("Rendered docs directory removed")


@task(name="compiled")
def clean_compiled(c):
    """
    Remove compilation artifacts.
    """

    def clean_dir(d):
        for entry in d.iterdir():
            if entry.name.endswith(".pyc"):
                entry.unlink()
            if entry.name == "__pycache__" or entry.name.endswith(".egg-info"):
                rmtree(entry)
                continue
            if entry.is_dir():
                clean_dir(entry)

    dirs_to_clean = [
        Path("./src").resolve(),
        Path("./tests").resolve(),
    ]
    for d in dirs_to_clean:
        echo(f"Removing compiled/cache artifacts in {str(d)}...")
        clean_dir(d)
    echo("Compiled artifacts and caches removed")


@task(name="tox")
def clean_tox(c):
    """
    Remove the .tox cache directory.
    """
    tox_dir = Path("./.tox").resolve()
    if tox_dir.exists() and tox_dir.is_dir():
        echo(f"Removing tox cache: {str(tox_dir)}...")
        rmtree(tox_dir)
        echo("Tox cache removed")
    else:
        echo(f"No docs cache dir found at {str(tox_dir)}")


@task(name="mypy")
def clean_mypy(c):
    """
    Remove the .mypy_cache directory.
    """
    mypy_cache_dir = Path("./.mypy_cache").resolve()
    if mypy_cache_dir.exists() and mypy_cache_dir.is_dir():
        echo(f"Removing mypy cache: {str(mypy_cache_dir)}...")
        rmtree(mypy_cache_dir)
        echo("Mypy cache removed")
    else:
        echo(f"No mypy cache dir found at {str(mypy_cache_dir)}")


@task(name="coverage")
def clean_coverage(c):
    """
    Remove the .coverage cache.
    """
    coverage_cache_file = Path("./.coverage").resolve()
    if coverage_cache_file.exists() and coverage_cache_file.is_file():
        echo(f"Removing coverage cache: {str(coverage_cache_file)}...")
        coverage_cache_file.unlink()
        echo("Coverage cache removed")
    else:
        echo(f"No coverage cache file found at {str(coverage_cache_file)}")


@task(name="wheelhouse")
def clean_wheelhouse(c):
    """
    Remove the wheelhouse.
    """
    wheelhouse_dir = Path("./wheelhouse").resolve()
    if wheelhouse_dir.exists() and wheelhouse_dir.is_dir():
        echo(f"Removing wheelhouse dir: {str(wheelhouse_dir)}...")
        rmtree(wheelhouse_dir)
        echo("Wheelhouse removed")
    else:
        echo(f"No wheelhouse dir found at {str(wheelhouse_dir)}")


@task(name="coverage-report")
def clean_coverage_report(c):
    """
    Remove the html coverage report.
    """
    coverage_report_dir = Path("./htmlcov").resolve()
    if coverage_report_dir.exists() and coverage_report_dir.is_dir():
        echo(f"Removing coverage report dir: {str(coverage_report_dir)}...")
        rmtree(coverage_report_dir)
        echo("Coverage report dir removed")
    else:
        echo(f"No coverage report dir found at {str(coverage_report_dir)}")


@task(name="all")
def clean_all(
    c,
    dists=True,
    docs=True,
    compiled=True,
    tox=True,
    mypy=True,
    coverage=True,
    wheelhouse=True,
    coverage_report=True,
):
    """
    Remove all clean-able artifacts.
    """
    if dists:
        clean_dists(c)
    if docs:
        clean_docs(c)
    if compiled:
        clean_compiled(c)
    if tox:
        clean_tox(c)
    if mypy:
        clean_mypy(c)
    if coverage:
        clean_coverage(c)
    if wheelhouse:
        clean_wheelhouse(c)
    if coverage_report:
        clean_coverage_report(c)


@task(name="dists")
def build_dists(c, clean=True):
    """
    Build distribution artifacts.
    """
    if clean:
        clean_dists(c)
    echo("Building dists...")
    c.run("python -m pep517.build -s -b .")
    echo(f"Dists now available in {Path('./dist').resolve()}")


@task(name="wheelhouse")
def build_wheelhouse(c, pindeps=True):
    """
    Build a dependency wheelhouse.
    """
    if pindeps:
        _pindeps(c)
    echo("Creating wheelhouse...")
    c.run("python -m pip wheel -w wheelhouse -r requirements.txt")
    echo(f"Wheelhouse now available in {Path('./wheelhouse').resolve()}")


@task(name="coverage-report")
def build_coverage_report(c, test=True):
    """
    Build an HTML coverage report.
    """
    if test:
        run_tests(c)
    echo("Creating coverage report...")
    c.run("coverage html")
    echo(f"Coverage report available at {str(Path('./htmlcov').resolve())}")


@task(name="todos")
def check_todos(c):
    """
    Check for `#TODO` comments in the code.
    """
    c.run("python -m pylint --disable=all --enable=W0511 src tests")


@task()
def release(c, prod=False, clean=True, build=True, skip_tests=False, autoformat=True):
    """
    Perform a release to pypi.
    """
    if autoformat:
        run_autoformatters(c)
    if not skip_tests:
        run_tests(c)
    if clean:
        clean_dists(c)
    if build:
        build_dists(c)
    cmd = "python -m twine upload"
    if not prod:
        echo("Uploading to test.pypi...")
        cmd += " --repository-url https://test.pypi.org/legacy"
    else:
        echo("--prod flag present. Uploading to pypi...")
    cmd += " ./dist/*"
    c.run(cmd)
    echo("Upload complete")


# Make implicit root explicit
ns = Collection()
# Apply some default configurations
ns.configure({"run": {"pty": True, "echo": True}})


# Root commands
ns.add_task(_pindeps)
ns.add_task(release)


# Define the "run" subcommand
run_ns = Collection("run")
run_ns.add_task(run_black)
run_ns.add_task(run_isort)
run_ns.add_task(run_tests)
run_ns.add_task(run_autoformatters)


# Define the "build" subcommand
build_ns = Collection("build")
build_ns.add_task(build_docs)
build_ns.add_task(build_dists)
build_ns.add_task(build_wheelhouse)
build_ns.add_task(build_coverage_report)


# Define the "clean" subcommand
clean_ns = Collection("clean")
clean_ns.add_task(clean_dists)
clean_ns.add_task(clean_docs)
clean_ns.add_task(clean_compiled)
clean_ns.add_task(clean_tox)
clean_ns.add_task(clean_mypy)
clean_ns.add_task(clean_coverage)
clean_ns.add_task(clean_wheelhouse)
clean_ns.add_task(clean_coverage_report)
clean_ns.add_task(clean_all)


# Define the "check" subcommand
check_ns = Collection("check")
check_ns.add_task(check_todos)


# Add custom subcommands to root namespace
ns.add_collection(run_ns)
ns.add_collection(build_ns)
ns.add_collection(clean_ns)
ns.add_collection(check_ns)
