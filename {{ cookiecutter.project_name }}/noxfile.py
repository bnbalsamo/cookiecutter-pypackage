"""Testing environments + steps."""
from os import environ

import nox

nox.options.error_on_external_run = True

ON_CI = bool(environ.get("CI"))

# If running on CI handle the version matrix in the CI config
# (Keep in sync w/ .github/workflows/test.yml LATEST_PYTHON + test matrix)
SUPPORTED_PYTHONS = None if ON_CI else ["3.8", "3.9", "3.10", "3.11"]


def install_package(session: nox.Session, *, use_wheel: bool = False) -> None:
    """
    Install the package, optionally using a prebuilt wheel.

    If `use_wheel` is True an appropriate wheel should exist in the `dist/` directory.
    """
    # Source install
    if not use_wheel:
        session.install(".")
        return
    # Wheel install
    # Install just the wheel
    # (be 100% sure we install the wheel from disk)
    session.install(
        "--find-links",
        "dist/",
        "--no-index",
        "--no-deps",
        "--only-binary",
        ":all:",
        "{{ cookiecutter.pip_name }}",
    )
    # Install the runtime dependencies
    session.install(
        "--find-links",
        "dist/",
        "{{ cookiecutter.pip_name }}",
    )


@nox.session(python=SUPPORTED_PYTHONS)  # type: ignore[misc]
def test(session: nox.Session) -> None:
    """Run the unit tests."""
    install_package(session, use_wheel=bool(environ.get("NOX_USE_WHEEL")))
    session.install("-r", "requirements/test_requirements.txt")
    session.run("python", "-m", "coverage", "run", "-m", "pytest", "tests/")
    # CI handles coverage data differently
    if not ON_CI:
        session.notify("coverage")


@nox.session  # type: ignore[misc]
def lint(session: nox.Session) -> None:
    """Run the linters."""
    session.install(".", "mypy", "pylint", "pre-commit")
    session.run("python", "-m", "pre_commit", "run", "--all-files")
    session.run("python", "-m", "pylint", "src")
    session.run("python", "-m", "mypy", "src")


@nox.session  # type: ignore[misc]
def docs(session: nox.Session) -> None:
    """Attempt to build the docs."""
    install_package(session, use_wheel=bool(environ.get("NOX_USE_WHEEL")))
    session.install("-r", "requirements/doc_requirements.txt")
    session.run("mkdocs", "build")


@nox.session  # type: ignore[misc]
def coverage(session: nox.Session) -> None:
    """Combine the coverage reports."""
    session.install("coverage[toml]")
    session.run("python", "-m", "coverage", "combine")
    session.run("python", "-m", "coverage", "report")
