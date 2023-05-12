"""Testing environments + steps."""
from argparse import ArgumentParser

import nox

nox.options.error_on_external_run = True

SUPPORTED_PYTHONS = ["3.8", "3.9", "3.10", "3.11"]


@nox.session(python=SUPPORTED_PYTHONS)  # type: ignore[misc]
def test(session: nox.Session) -> None:
    """Run the unit tests."""
    parser = ArgumentParser()
    parser.add_argument("-a", "--artifact", default=".")
    parser.add_argument("-p", "--test-paths", nargs="+", default=["tests/"])
    args, _ = parser.parse_known_args(session.posargs)
    session.install(args.artifact, "-r", "requirements/test_requirements.txt")
    session.run("python", "-m", "coverage", "run", "-m", "pytest", *args.test_paths)
    session.notify("coverage")


@nox.session  # type: ignore[misc]
def introspect(session: nox.Session) -> None:
    """Run code introspection that requires the project be installed."""
    session.install(".", "mypy", "pylint")
    session.run("python", "-m", "pylint", "src")
    session.run("python", "-m", "mypy", "src")


@nox.session  # type: ignore[misc]
def lint(session: nox.Session) -> None:
    """Run the linters."""
    session.install("pre-commit")
    session.run("python", "-m", "pre_commit", "run", "--all-files")


@nox.session  # type: ignore[misc]
def docs(session: nox.Session) -> None:
    """Attempt to build the docs."""
    parser = ArgumentParser()
    parser.add_argument("-a", "--artifact", default=".")
    args, _ = parser.parse_known_args(session.posargs)
    session.install(args.artifact, "-r", "requirements/doc_requirements.txt")
    session.run("mkdocs", "build")


@nox.session  # type: ignore[misc]
def coverage(session: nox.Session) -> None:
    """Combine the coverage reports."""
    session.install("coverage[toml]")
    session.run("python", "-m", "coverage", "combine")
    session.run("python", "-m", "coverage", "report")
