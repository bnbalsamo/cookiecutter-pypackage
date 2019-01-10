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
    print("Done")


main()
exit(0)
