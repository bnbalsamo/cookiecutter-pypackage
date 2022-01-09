"""Noxfile."""
import tempfile
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import List

import nox
import nox_poetry
from nox_poetry.sessions import Session

nox.options.sessions = [
    "test",
    "pre_commit",
    "pylint",
    "mypy",
    "safety",
    "build",
    "docs",
    "docs_linkcheck",
]
nox.options.error_on_missing_interpreters = False
nox.options.error_on_external_run = True


# Python versions the package supports
SUPPORTED_PYTHONS: List[str] = [
    "3.10",
    "3.9",
    "3.8",
    "3.7",
]


# Dependencies imported in either noxfile.py or tasks.py
# (required so mypy and pylint can accurately parse these files)
IMPORTED_DEV_REQUIREMENTS = [
    "invoke",
    "nox",
    "packaging",
    "nox-poetry",
]


@nox_poetry.session(python=SUPPORTED_PYTHONS)
def test(session: Session) -> None:
    """Run the unit tests."""
    # Remove the coverage file if it exists
    coverage_file = Path(".coverage")
    if coverage_file.exists():
        coverage_file.unlink()

    session.install(".[tests]")
    session.run("coverage", "run", "-p", "--branch", "-m", "pytest")
    session.notify("coverage")


@nox_poetry.session
def coverage(session: Session) -> None:
    """Generate combined coverage metrics."""
    session.install("coverage[toml]")
    session.run("coverage", "combine")
    session.run("coverage", "report")


@nox_poetry.session
def pre_commit(session: Session) -> None:
    """Run pre-commit against all files."""
    session.install("pre-commit")
    session.run(
        "python", "-m", "pre_commit", "run", "--all-files", "--show-diff-on-failure"
    )


@nox_poetry.session
def pylint(session: Session) -> None:
    """Run pylint."""
    session.install(".[docs,tests]")
    session.install("pylint")
    session.install(*IMPORTED_DEV_REQUIREMENTS)
    session.run(
        "python",
        "-m",
        "pylint",
        "src/",
        "tests/",
        "tasks.py",
        "noxfile.py",
    )


@nox_poetry.session
def mypy(session: Session) -> None:
    """Run mypy."""
    session.install(".[docs,tests]", *IMPORTED_DEV_REQUIREMENTS)
    # Can't typecheck tasks.py until the following is fixed:
    # https://github.com/pyinvoke/invoke/issues/357
    session.install("mypy")
    session.run(
        "python",
        "-m",
        "mypy",
        "--non-interactive",
        "--install-types",
        "--scripts-are-modules",
        "src/",
        "tests/",
        "noxfile.py",
    )


@nox_poetry.session
def safety(session: Session) -> None:
    """Run safety against the installed environment."""
    session.install(".")
    # Update what comes packaged in the venv
    session.run_always("pip", "install", "-U", "pip", "setuptools", "wheel")
    session.install("safety")
    session.run("python", "-m", "safety", "check")


@nox_poetry.session
def build(session: Session) -> None:
    """Check that the package builds properly."""
    session.install("build", "twine")
    with TemporaryDirectory() as tmp_dir:
        session.run("python", "-m", "build", "--outdir", tmp_dir, ".")
        session.run("python", "-m", "twine", "check", tmp_dir + "/*")


@nox_poetry.session
def docs(session: Session) -> None:
    """Check that the docs build properly."""
    session.install(".[docs]")
    with tempfile.TemporaryDirectory() as tmp_dir:
        session.run(
            "sphinx-build",
            "-d",
            f"{tmp_dir}/docs_doctree",
            "docs",
            f"{tmp_dir}/docs_out",
            "--color",
            "-W",
            "-bhtml",
        )


@nox_poetry.session
def docs_linkcheck(session: Session) -> None:
    """Check there are no dead links in the docs."""
    session.install(".[docs]")
    with tempfile.TemporaryDirectory() as tmp_dir:
        session.run(
            "sphinx-build",
            "-d",
            f"{tmp_dir}/docs_doctree",
            "docs",
            f"{tmp_dir}/docs_out",
            "--color",
            "-W",
            "-blinkcheck",
        )
