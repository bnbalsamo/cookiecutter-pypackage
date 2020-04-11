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


def main():
    if '{{ cookiecutter.create_docs_folder }}' != 'y':
        remove_docs_folder()
    print("Template successfully created.\n")
    print("""!!! SETUP !!!

# Install any required versions of python, if not already installed
eg: $ pyenv install-latest 3.7
# Create a virtualenv for your project
eg: $ pyenv virtualenv 3.7.x {{ cookiecutter.slug_name }}
# Change to the project directory
$ cd {{ cookiecutter.project_name }}
# Set your local python environment
$ pyenv local {{ cookiecutter.slug_name }} 3.7.x # include all versions tox will need
# Install all the required utilities
$ pip install -r requirements/requirements_dev.txt
# Initialize your git repository
$ git init
# Add everything to git
$ git add {.[!.]*,*}
$ git commit -m "First commit!"
# Add your remote repo and push (change URI if not using a personal github account)
$ git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.git
$ git push -u origin master
""")
    print("Happy Developing!")


main()
exit(0)
