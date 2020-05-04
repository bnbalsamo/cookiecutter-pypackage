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


@task(name="pindeps")
def _pindeps(c):
    """
    Pin dependencies, creating or overwriting requirements.txt
    """
    # Requires being run in a fresh virtualenv,
    # so we leverage tox
    c.run("tox -e pindeps --recreate")


@task(name="black")
def run_black(c):
    """
    Run `black` to autoformat the source code.
    """
    # The result of this command should satisfy the
    # corresponding tox testenv check_black
    c.run("python -m black ./src ./tests")


@task(name="isort")
def run_isort(c):
    """
    Run `isort` to autoformat the source code.
    """
    # The result of this command should satisfy the
    # corresponding tox testenv check_isort
    c.run("python -m isort -rc ./src ./tests")


@task(name="autoformatters")
def run_autoformatters(c):
    """
    Run all the autoformatters.
    """
    run_black(c)
    run_isort(c)


@task(name="tests")
def run_tests(c, autoformat=True):
    """
    Run the tests.
    """
    if autoformat:
        run_autoformatters(c)
    c.run("tox")


@task(name="docs")
def build_docs(c, clean=True, buildername="html"):
    """
    Build the documentation.
    """
    if clean:
        clean_docs(c)
    c.run(f"sphinx-build docs docs_out --color -W -b{buildername}")


@task(name="dists")
def clean_dists(c):
    """
    Remove existing distributions.
    """
    dist_dir = Path("./dist").resolve()
    if not dist_dir.exists():
        return
    if not dist_dir.is_dir():
        raise NotADirectoryError(dist_dir)
    print(f"Removing existing dist dir: {str(dist_dir)}")
    for contents in dist_dir.iterdir():
        contents.unlink()
    dist_dir.rmdir()


@task(name="docs")
def clean_docs(c):
    """
    Remove existing docs.
    """
    docs_out_dir = Path("./docs_out").resolve()
    if not docs_out_dir.exists():
        return
    if not docs_out_dir.is_dir():
        raise NotADirectoryError(docs_out_dir)
    print(f"Removing existing rendered docs dir: {str(docs_out_dir)}")
    rmtree(docs_out_dir)


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
        print(f"Cleaning dir {str(d)}")
        clean_dir(d)


@task(name="all")
def clean_all(c, dists=True, docs=True, compiled=True):
    """
    Remove all clean-able artifacts.
    """
    if dists:
        clean_dists(c)
    if docs:
        clean_docs(c)
    if compiled:
        clean_compiled(c)


@task(name="dists")
def build_dists(c, clean=True):
    """
    Build distribution artifacts.
    """
    if clean:
        clean_dists(c)
    print("Building dists...")
    c.run("python -m pep517.build -s -b .")
    print(f"Dists now available in {Path('./dist').resolve()}")


@task(name="wheelhouse")
def build_wheelhouse(c, pindeps=True):
    """
    Build a dependency wheelhouse.
    """
    if pindeps:
        _pindeps(c)
    print("Creating wheelhouse...")
    c.run("python -m pip wheel -w wheelhouse -r requirements.txt")
    print(f"Wheelhouse now available in {Path('./wheelhouse').resolve()}")


@task()
def release(c, prod=False, clean=True, build=True, skip_tests=False):
    """
    Perform a release to pypi.
    """
    if not skip_tests:
        run_tests(c)
    if clean:
        clean_dists(c)
    if build:
        build_dists(c)
    cmd = "python -m twine upload"
    if not prod:
        cmd += " --repository-url https://test.pypi.org/legacy"
    cmd += " ./dist/*"
    c.run(cmd)


# Make implicit root explicit
ns = Collection()


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


# Define the "clean" subcommand
clean_ns = Collection("clean")
clean_ns.add_task(clean_dists)
clean_ns.add_task(clean_docs)
clean_ns.add_task(clean_compiled)
clean_ns.add_task(clean_all)


# Add custom subcommands to root namespace
ns.add_collection(run_ns)
ns.add_collection(build_ns)
ns.add_collection(clean_ns)
