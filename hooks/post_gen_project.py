from textwrap import dedent


def print_setup_instructions():
    print(dedent("""\
    !!! SETUP !!!

    -> Please complete setup via either the manual steps *OR* the automatic script. <-

    # Manual Steps

    - Configure a venv with an appropriate version of python
    - Activate the venv
    - Upgrade pip within the venv
    - Configure tox to have access to all relevant versions of python
    - Install the package in editable mode + all extras
    - Initialize a git repo and all the files within your project directory
    - Push the contents of your local repo to the appropriate github repo

    # Automatic Setup

    -> Copy/paste the following into your terminal, or manually complete setup. <-
    -> This requires pyenv, pyenv-virtualenv, and xxenv-latest be installed <-

    [[ `type -t pyenv` ]] && \\
    [ -s "$PYENV_ROOT/plugins/pyenv-virtualenv" ] && \\
    [ -s "$PYENV_ROOT/plugins/xxenv-latest" ] && \\
    PROJECT_NAME="{{ cookiecutter.project_name }}" && \\
    pyenv latest install -s 3.8 && \\
    PYENV_LATEST_38=$(pyenv latest -p 3.8) && \\
    pyenv latest install -s 3.7 && \\
    PYENV_LATEST_37=$(pyenv latest -p 3.7) && \\
    pyenv latest install -s 3.6 && \\
    PYENV_LATEST_36=$(pyenv latest -p 3.6) && \\
    cd $PROJECT_NAME && \\
    git init && \\
    git add {.[!.]*,*} && \\
    git commit -m "first commit" && \\
    git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.git && \\
    git push -u origin {{ cookiecutter.github_default_branch_name }} && \\
    pyenv virtualenv "$PYENV_LATEST_38" "$PROJECT_NAME" && \\
    pyenv local "$PROJECT_NAME" "$PYENV_LATEST_38" "$PYENV_LATEST_37" "$PYENV_LATEST_36" && \\
    python -m pip install -U pip wheel && \\
    python -m pip install -e .[dev,tests,docs]
    """))


print("Template successfully created.\n")
print_setup_instructions()
print("Happy Developing!\n")
exit(0)
