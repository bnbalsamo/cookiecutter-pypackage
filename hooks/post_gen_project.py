import os


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath):
    os.rmdir(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_docs_folder():
    for x in ['autodoc.rst', 'conf.py', 'index.rst',
              'make.bat', 'Makefile']:
        remove_file(os.path.join("docs", x))
    for x in ['_build', '_static', '_templates']:
        remove_file(os.path.join("docs", x, ".gitinclude"))
        remove_dir(os.path.join("docs", x))
    remove_dir("docs")

def print_setup_instructions():
    print("""!!! SETUP !!!

-> Please complete setup via either the manual steps *OR* the automatic script. <-

# Manual Steps

- Configure a venv with an appropriate version of python
- Configure tox to have access to all relevant versions of python
- Install the contents of requirements/requirements_dev.txt into the venv
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
git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.git && \\
git push -u origin {{ cookiecutter.github_default_branch_name }} && \
pyenv virtualenv "$PYENV_LATEST_38" "$PROJECT_NAME" && \\
pyenv local "$PROJECT_NAME" "$PYENV_LATEST_38" "$PYENV_LATEST_37" "$PYENV_LATEST_36" && \\
pip install -r "requirements/requirements_dev.txt"
""")
    print()

def main():
    if '{{ cookiecutter.create_docs_folder }}' != 'y':
        remove_docs_folder()
    print("Template successfully created.\n")
    print_setup_instructions()
    print("Happy Developing!")


main()
exit(0)
