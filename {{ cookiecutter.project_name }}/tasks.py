"""Development tasks."""
import os
from pathlib import Path
from typing import cast

import invoke

os.chdir(Path(__file__).parent.resolve())


@invoke.task
def install(ctx):  # type: ignore[no-untyped-def]
    """Install the package in editable mode."""
    ctx.run("python -m pip install -e .")


@invoke.task
def clean(ctx):  # type: ignore[no-untyped-def]
    """Remove previously built distributions."""
    if Path("dist/").exists():
        ctx.run("rm -r dist/")


@invoke.task(pre=[clean])
def build(ctx):  # type: ignore[no-untyped-def]
    """Build a wheel and sdist."""
    ctx.run("python -m build")
    ctx.run("python -m twine check dist/*")


@invoke.task(pre=[build])
def test(ctx):  # type: ignore[no-untyped-def]
    """Run the tests."""
    ctx.run("python -m nox -- -a dist/*.whl", pty=True)


@invoke.task
def lint(ctx):  # type: ignore[no-untyped-def]
    """Lint (and autoformat) the source."""
    ctx.run("python -m pre_commit run --all-files", pty=True)


def _get_next_version(ctx: invoke.Context, bumpver_cmd: str) -> str:
    """Get the next version of the project, computed by bumpver."""
    line_prefix = "INFO    - New Version: "
    bumpver_cmd += " -d > /dev/null"
    bumpver_output = ctx.run(bumpver_cmd).stderr
    for line in bumpver_output.splitlines():
        if line.startswith(line_prefix):
            new_ver_line = line
            break
    else:
        msg = f"Could not determine next version from bumpver output: {bumpver_output}"
        raise RuntimeError(msg)
    return cast(str, new_ver_line[len(line_prefix) :].strip())


@invoke.task
def prepare(ctx, *, hotfix=False):  # type: ignore[no-untyped-def]
    """Prepare the repository for a release."""
    # Compute the next version ahead of time, so we can give it to towncrier.
    bumpver_cmd = "python -m bumpver update"
    if hotfix:
        bumpver_cmd += " --pin-increments --pin-date -t post --tag-num"
    else:
        bumpver_cmd += " -t final"

    # Towncrier
    next_version = _get_next_version(ctx, bumpver_cmd)
    ctx.run(f"python -m towncrier build --yes --version {next_version}")
    # Towncrier stages but doesn't commit
    ctx.run(f"git commit -m 'rendering newsfragments for release {next_version}'")

    # Bumpver
    ctx.run(bumpver_cmd)


@invoke.task(pre=[build])
def publish(ctx):  # type: ignore[no-untyped-def]
    """Publish built artifacts to pypi."""
    twine_cmd = "python -m twine upload dist/* "
    if os.environ.get("CI") is None:
        maybe_continue = input(
            "It looks like you're not the CI server. "
            "Please type 'continue' to continue: "
        )
        if maybe_continue.strip() != "continue":
            msg = "Exiting..."
            raise SystemExit(msg)
    else:
        twine_cmd += "--non-interactive --disable-progress-bar "

    prod_pypi = "https://upload.pypi.org/legacy/"
    twine_cmd += f"--repository-url {prod_pypi} "

    # Upload package
    ctx.run(twine_cmd)

    # Deploy docs
    ctx.run("mkdocs gh-deploy --force")
