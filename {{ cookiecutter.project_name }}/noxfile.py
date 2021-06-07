"""Noxfile."""
import tempfile
from tempfile import TemporaryDirectory
from typing import Any, List

import nox
from nox.sessions import Session
from packaging.requirements import Requirement

nox.options.error_on_missing_interpreters = False
nox.options.error_on_external_run = True


# Python versions the package supports
SUPPORTED_PYTHONS: List[str] = [
    "3.9",
    "3.8",
    "3.7",
    "3.6",
]


# Requirements to build the docs
DOCS_REQUIREMENTS: List[str] = [
    "sphinx",
    "sphinx-rtd-theme",
    "sphinx-autodoc-typehints",
]


# Requirements to run the tests
TESTS_REQUIREMENTS: List[str] = [
    "pytest",
    "pytest-cov",
]


# Requirements to run the development tasks
TASKS_REQUIREMENTS: List[str] = [
    "invoke",
]


# Requirements to run nox
NOX_REQUIREMENTS: List[str] = [
    "nox",
    "packaging",
]


def install_with_constraints(
    session: Session, *args: Any, allow_unlocked: bool = False, **kwargs: Any
) -> None:
    """
    Install packages constrained by Poetry's lock file.

    This function is a wrapper for nox.sessions.Session.install. It
    invokes pip to install packages inside of the session's virtualenv.
    Additionally, pip is passed a constraints file generated from
    Poetry's lock file, to ensure that the packages are pinned to the
    versions specified in poetry.lock. This allows you to manage the
    packages as Poetry development dependencies.

    Arguments:
        session: The Session object.
        args: Command-line arguments for pip.
        allow_unlocked: If true allow installing dependencies that don't
            exist in the poetry lock file.
        kwargs: Additional keyword arguments for Session.install.
    """
    with tempfile.NamedTemporaryFile(mode="w") as tmp_file:
        req_path = tmp_file.name
        session.run(
            "poetry",
            "export",
            "--dev",
            "--without-hashes",
            "--format=requirements.txt",
            f"--output={req_path}",
            external=True,
        )

        # Confirm the requested package exists in the poetry.lock file
        if not allow_unlocked:
            pinned_names = []
            with open(req_path) as req_file:
                for line in req_file.readlines():
                    pinned_names.append(Requirement(line).name)
            for name in args:
                if Requirement(name).name not in pinned_names:
                    raise RuntimeError(f"{name} missing from poetry.lock!")
        # Install the package via pip
        session.install(f"--constraint={req_path}", *args, **kwargs)


@nox.session(python=SUPPORTED_PYTHONS)
def test(session: Session) -> None:
    """Run the unit tests."""
    session.run_always("poetry", "install", "--no-dev", external=True)
    install_with_constraints(session, *TESTS_REQUIREMENTS)
    session.run("pytest", "--cov={{ cookiecutter.module_name }}", "--cov-append")


@nox.session
def pre_commit(session: Session) -> None:
    """Run pre-commit against all files."""
    install_with_constraints(session, "pre-commit")
    session.run(
        "python", "-m", "pre_commit", "run", "--all-files", "--show-diff-on-failure"
    )


@nox.session
def pylint(session: Session) -> None:
    """Run pylint."""
    session.run_always("poetry", "install", "--no-dev", external=True)
    install_with_constraints(
        session,
        "pylint",
        *TESTS_REQUIREMENTS,
        *TASKS_REQUIREMENTS,
        *NOX_REQUIREMENTS,
    )
    session.run(
        "python",
        "-m",
        "pylint",
        "src/",
        "tests/",
        "tasks.py",
        "noxfile.py",
    )


@nox.session
def mypy(session: Session) -> None:
    """Run mypy."""
    session.run_always("poetry", "install", "--no-dev", external=True)
    install_with_constraints(
        session,
        "mypy",
        *TESTS_REQUIREMENTS,
        *NOX_REQUIREMENTS,
    )
    # Can't typecheck tasks.py until the following is fixed:
    # https://github.com/pyinvoke/invoke/issues/357
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


@nox.session
def safety(session: Session) -> None:
    """Run safety against the installed environment."""
    session.run_always("poetry", "install", "--no-dev", external=True)
    # Update what comes packaged in the venv
    session.run_always("pip", "install", "-U", "pip", "setuptools", "wheel")
    install_with_constraints(session, "safety")
    session.run("python", "-m", "safety", "check")


@nox.session
def build(session: Session) -> None:
    """Check that the package builds properly."""
    install_with_constraints(session, "build", "twine")
    with TemporaryDirectory() as tmp_dir:
        session.run("python", "-m", "build", "--outdir", tmp_dir, ".")
        session.run("python", "-m", "twine", "check", tmp_dir + "/*")


@nox.session
def docs(session: Session) -> None:
    """Check that the docs build properly."""
    session.run_always("poetry", "install", "--no-dev", external=True)
    install_with_constraints(session, *DOCS_REQUIREMENTS)
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


@nox.session
def docs_linkcheck(session: Session) -> None:
    """Check there are no dead links in the docs."""
    session.run_always("poetry", "install", "--no-dev", external=True)
    install_with_constraints(session, *DOCS_REQUIREMENTS)
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
