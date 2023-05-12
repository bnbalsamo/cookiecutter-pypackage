"""
Post generation script.

Template variables in this script will be substituted before execution.

When this script executes the template will be rendered, and the working directory
will be set to the root of the rendered template.
"""

from pathlib import Path
from textwrap import dedent


def print_setup_instructions():
    print(
        dedent(
            f"""\
            !!! SETUP !!!

            cd "{{ cookiecutter.project_name }}" && \\
            python -m venv venv && \\
            source venv/bin/activate && \\
            python -m pip install -r requirements/dev_requirements.txt && \\
            git init && \\
            python -m pre_commit autoupdate && \\
            git add {" ".join(entry.name for entry in Path(".").iterdir())} && \\
            git commit -m "initial template render" && \\
            python -m invoke install && \\
            python -m pre_commit install --install-hooks && \\
            git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.git && \\
            git push -u origin main
            """
        )
    )


print("Template successfully created.\n")
print_setup_instructions()
print("Please review the license file (and pyproject.toml classifier) and make any appropriate changes.\n")
print("Remember to add a `PYPI_TOKEN` secret to the repo!\n")
print("Happy Developing!\n")
exit(0)