from sys import version_info
from os import getcwd
from os.path import join


def make_venv():
    if version_info < (3, 3):
        # Can't build the venv, alert but don't fail.
        print("Incompatible Python (<3.3). " +
              "Virtual environment must be created manually\n")
        return

    from venv import main

    cookiecutter_args = "{{cookiecutter.venv_args}}"
    args = "{}".format(join(getcwd(), '.env'))
    if cookiecutter_args != "":
        args = "{} {}".format(cookiecutter_args, args)
    main(args.split())
    print("Virtual environment successfully created. Activate " +
          "it with: \n" +
          "$ source .env/bin/activate \n" +
          "from the project root\n")


def main():
    print("Template successfully created.\n")
    make_venv()
    print("Done")

main()
exit(0)
