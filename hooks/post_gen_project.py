from sys import version_info
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
        remove_dir(os.path.join("docs", x))
    remove_dir("docs")


def make_venv():
    if version_info < (3, 3):
        # Can't build the venv, alert but don't fail.
        print("Incompatible Python (<3.3). " +
              "Virtual environment must be created manually\n")
        return

    from venv import main

    cookiecutter_args = "{{cookiecutter.venv_args}}"
    args = "{}".format(os.path.join(PROJECT_DIRECTORY, 'venv'))
    if cookiecutter_args != "":
        args = "{} {}".format(cookiecutter_args, args)
    main(args.split())
    print("Virtual environment successfully created. Activate " +
          "it with: \n" +
          "$ source venv/bin/activate \n" +
          "from the project root\n")


def main():
    if '{{ cookiecutter.create_docs_folder }}' != 'y':
        remove_docs_folder()
    print("Template successfully created.\n")
    make_venv()
    print("Done")


main()
exit(0)
