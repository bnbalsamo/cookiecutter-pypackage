from textwrap import dedent


def print_setup_instructions():
    print(
        dedent(
            """\
    !!! SETUP !!!

    -> Please complete setup via either the manual steps *OR* the automatic script. <-

    # Manual Steps

    - cd into the project directory
    - Create a git repository, add all the created files
    - Install the project with poetry
    - Install the pre-commit hooks
    - Push the contents of your local repo to the appropriate github repo

    # Automatic Setup

    -> Copy/paste the following into your terminal, or manually complete setup. <-
    -> This requires poetry be installed <-

    ([[ `type -t poetry` ]] || (echo poetry not installed && exit 1)) && \\
    cd "{{ cookiecutter.project_name }}" && \\
    git init && \\
    git add {.[!.]*,*} && \\
    git commit -m "initial template render" && \\
    poetry install && \\
    git add poetry.lock && \\
    git commit -m "Adding initial lock file" && \\
    poetry run pre-commit install --install-hooks && \\
    git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.git && \\
    git push -u origin {{ cookiecutter.github_default_branch_name }}
    """
        )
    )


print("Template successfully created.\n")
print_setup_instructions()
print("Happy Developing!\n")
exit(0)
