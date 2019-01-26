# cookiecutter-pypackage [![v0.11.0](https://img.shields.io/badge/version-0.11.0-blue.svg)](https://github.com/bnbalsamo/cookiecutter-pypackage/releases)

[![Build Status](https://travis-ci.org/bnbalsamo/cookiecutter-pypackage.svg?branch=master)](https://travis-ci.org/bnbalsamo/cookiecutter-pypackage)

My [cookiecutter](https://github.com/audreyr/cookiecutter) template for python packages

# Whats it get me?
- [Github](https://github.com/) integration
- [TravisCI](https://travis-ci.org/) integration
    - Optional support for testing multiple versions of python by adding to the python array in ```.travis.yml```
- [Coveralls](https://coveralls.io/) integration
- [pyup](https://pyup.io/) integration
- Testing via [tox](https://tox.readthedocs.io/en/latest/)
- A minimal README + badges
- (optional) [Sphinx](http://www.sphinx-doc.org) documentation
    - With a minimal autodocs setup
    - Ready for use with [readthedocs](https://readthedocs.org/)
- Packages for common development tasks
    - [pip](https://pip.pypa.io/en/latest/)
    - [bumpversion](https://github.com/peritus/bumpversion)
    - [wheel](http://pythonwheels.com/)
    - [flake8](http://flake8.pycqa.org/en/latest/)
    - [coverage](https://coverage.readthedocs.io/en/latest/)
    - [pytest](https://docs.pytest.org/en/latest/)
    - [twine](https://pypi.python.org/pypi/twine)
    - [check-manifest](https://github.com/mgedmin/check-manifest)
    - [isort](https://github.com/timothycrosley/isort)
    - [bandit](https://github.com/PyCQA/bandit)
    - [pydocstyle](www.pydocstyle.org/en/latest/)
    - [safety](https://pyup.io/docs/safety/installation-and-usage/)

# Quickstart

- Requirements For These Instructions
    - [Cookiecutter](https://github.com/audreyr/cookiecutter)
    - [Github](https://github.com/) account
    - [TravisCI](https://travis-ci.org/) account
    - [Coveralls](https://coveralls.io/) account
    - [readthedocs](https://readthedocs.org/) account
    - [pyup](https://pyup.io/) account
    - [pyenv](https://github.com/pyenv/pyenv)
    - [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
        - [pyenv-install-latest](https://github.com/momo-lab/pyenv-install-latest) is also handy
    - Install the requesite python interpreters in pyenv
        - ```$ pyenv install-latest 3.7``` for instance
- Steps
    - Create a github repo named $YOUR_PROJECT_NAME
    - Enable repository monitoring on Travis
    - Enable repository monitoring on coveralls
    - Enable repository monitoring on readthedocs
    - Enable repository monitoring in pyup
    - ```$ cookiecutter gh:bnbalsamo/cookiecutter-pypackage```
    - Fill in the prompts
    - ```$ cd $YOUR_PROJECT_NAME```
    - ```$ pyenv-virtualenv $WHATEVER_PYTHON_VERSION $SLUG_NAME```
    - ```$ pyenv local $SLUG_NAME $ALL_PY_VERSIONS_TO_EXPOSE_TO_TOX```
    - ```$ pip install -r requirements/requirements_dev.txt```
    - ```$ git init```
    - ```$ git add .```
    - ```$ git commit -m "first commit"```
    - ```$ check-manifest -c```
    - ```$ git add MANIFEST.in```
    - ```$ git commit -m "Adding MANIFEST.in"```
    - ```$ git remote add origin $YOUR_REPO_ADDRESS```
    - ```$ git push -u origin master```
    - Begin developing your package!

# Functionalities

Any of the following can be run off the bat from the project root

* ```tox```: Run tests, generate coverage stats, run flake8, run pydocstyle, run an isort check, run bandit
* ```tox -lv```: List all available tox environments
* ```tox -e pindeps```: Generate a ```requirements.txt``` with pinned dependencies.
* ```bumpversion $PART```: Bump the version number of the project
    * ```git push && git push --tags``` to upload/release to git
* ```autopep8 .```: Automatically fix some pep8 errors
* ``` check-manifest .```: Check that your manifest file is correct
    * the ```-c``` option will create one, if it doesn't exist
    * the ```-u``` option will update an existing file, or create one
* ```isort -rc --atomic --apply $YOUR_PROJECT_DIR```: Automatically sort your imports

## Uploading to pypi

I'll not hazard a short answer here, as there are too many options.

[This](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/) blog
entry provides a good breakdown of uploading a package to pypi. All of the referenced
tools should be installed by a ```pip -r requirements/requirements_dev.txt``` in your project
virtualenv.


## Credit Where It's Due

Inspiration (and some code) taken from the following:
* [audreyr's pypackage template](https://github.com/audreyr/cookiecutter-pypackage)
* [kennethreitz setup.py template](https://github.com/kennethreitz/setup.py/blob/master/setup.py)
* [kennethreitz's blog post "A Better Pip Workflow"](https://www.kennethreitz.org/essays/a-better-pip-workflow)
* [Donald Stufft's blog post about setup.py vs requirements.txt](https://caremad.io/posts/2013/07/setup-vs-requirement/)
* All the wonderful folks writing the tools and services involved in this template and their documentation!
