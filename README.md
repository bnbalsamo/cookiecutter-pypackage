# cookiecutter-pypackage [![v0.18.2](https://img.shields.io/badge/version-0.18.2-blue.svg)](https://github.com/bnbalsamo/cookiecutter-pypackage/releases)

[![Build Status](https://travis-ci.org/bnbalsamo/cookiecutter-pypackage.svg?branch=master)](https://travis-ci.org/bnbalsamo/cookiecutter-pypackage)

My [cookiecutter](https://github.com/audreyr/cookiecutter) template for python packages

# Whats it get me?

tl;dr: A CI enabled Python software project with plenty of bells and whistles.

- [Github](https://github.com/) integration
- [TravisCI](https://travis-ci.org/) integration
    - Optional support for testing multiple versions of python by adding to the python array in ```.travis.yml```
- [Coveralls](https://coveralls.io/) integration
- [pyup](https://pyup.io/) integration
- Testing via [tox](https://tox.readthedocs.io/en/latest/)
- Tox environments to facilitate...
    - Running autoformatters like black and isort
    - Easily check `#TODO` comments
    - Building documentation
    - Pin depedencies to a `requirements.txt`
    - Test release to pypi
    - Release to pypi
    - Build source distributions and wheels
    - Build wheelhouses of your projects dependencies
- A minimal README + relevant badges
- (optional) [Sphinx](http://www.sphinx-doc.org) documentation
    - With a minimal autodocs setup
    - Ready for use with [readthedocs](https://readthedocs.org/)
- All the tooling you can shake a stick at, wrapped up in a ```tox``` config
    - [pytest](https://docs.pytest.org/en/latest/)
    - [flake8](http://flake8.pycqa.org/en/latest/)
    - [pylint](https://www.pylint.org)
    - [coverage](https://coverage.readthedocs.io/en/latest/)
    - [twine](https://pypi.python.org/pypi/twine)
    - [check-manifest](https://github.com/mgedmin/check-manifest)
    - [isort](https://github.com/timothycrosley/isort)
    - [bandit](https://github.com/PyCQA/bandit)
    - [pydocstyle](www.pydocstyle.org/en/latest/)
    - [safety](https://pyup.io/docs/safety/installation-and-usage/)
    - [black](https://github.com/ambv/black)
    - [mypy](http://mypy-lang.org/)

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
    - ```$ git add {.[!.]*,*}```
    - ```$ git commit -m "first commit"```
    - ```$ git remote add origin $YOUR_REPO_ADDRESS```
    - ```$ git push -u origin master```
    - Begin developing your package!

# Functionalities

Any of the following can be run off the bat from the project root

* ```tox```:
  * Run ```pytest```
  * generate coverage metrics
  * run ```flake8```
  * run ```pydocstyle```
  * run an ```isort``` check
  * run a ```bandit``` check
  * run a ```black``` check
  * run a ```safety``` check
  * run a ```checkmanifest``` check
  * run a ```mypy``` check
  * build the sphinx documentation
* ```tox -e check_todos```: List all of the `# TODO` comment lines in the code
* ```tox -e pindeps```: Generate a ```requirements.txt``` with pinned dependencies
* ```tox -e run_isort```: Run isort on the codebase
* ```tox -e run_black```: Run black on the codebase
* ```tox -e build```: Build distribution packages
* ```tox -e build_wheelhouse```: Build a wheelhouse of project dependencies
* ```tox -e test_release```: Test releasing (with test.pypi.org)
* ```tox -e release```: Release to pypi
* ```bumpversion $PART```: Bump the version number of the project
  * ```git push && git push --tags``` to upload/release to git

## Uploading to pypi

Review your package before publishing it!

[This](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/) blog
entry provides a good breakdown of uploading a package to pypi.

This template provides several handy tox environments for packaging.

* ```tox -e build```: Populates the dist/ folder with an sdist and bdist
* ```tox -e test_release```: Perform a test release to https://test.pypi.org
* ```tox -e release```: Perform a realease to PyPI.

# Opinions

This template is opinionated (aren't they all, really?) in a couple of ways.

It keeps all of the static analysis tooling dialed up _fairly_ strictly.

This isn't meant to imply that every project should keep the static analysis tooling
dialed up so strictly, but rather that if you are loosening controls on your static analysis
for a good reason that reason should be documented as a part of your codebase's git history.
This helps keep relevant decisions documented with the code.

It causes testing to fail below 80% code coverage.

80% is arbitrary, but I've found it works fairly well for me when starting a project. If while
I'm actively developing and the code base is small I fall below 80% coverage I know I've
probably slacked off on tests somewhere. As a codebase grows and matures I tend to turn this
metric up to whatever reasonable maximum I can hit.

It uses requirements.txt rather than Pipfile and Pipfile.lock.

I made this decision because the pipfile specification isn't integrated into pip (yet),
because it allows for fewer differences between developing applications and libraries,
and because I don't particularly like the fact that the existing tools attempt
to be a "one stop shop" for managing dependency declarations and virtualenvs.

It implements a lot of tooling.

Well, thats the whole reason for the use of a cookiecutter, isn't it? I'm of the opinion
that even if a project chooses not use every tool in this template, it's easier to rip out
a few pieces here and there than it is to properly re-implement them. Thus I've tended to err
on the side of including tooling, rather than omitting it.

It uses web service X instead of competing service Y.

My choice of services is informed by:
- What services I'm comfortable with implementing
- What services appear to be popular within the python community
If the services this repository implement are (significantly) eclipsed by similar services
in the future open an issue and let me know!

It uses [semver](https://semver.org/) for versioning.

I'm of the opinion that semver is applicable to the vast majority of projects. If, for whatever
reason, it isn't applicable to a given project, changing the versioning scheme along with the
justification should be included in the git history.

It uses a "src" layout

I've [been](https://hynek.me/articles/testing-packaging/) [convinced](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure).

# Credit Where It's Due

Inspiration (and some code) taken from the following:
* [audreyr's pypackage template](https://github.com/audreyr/cookiecutter-pypackage)
* [kennethreitz setup.py template](https://github.com/kennethreitz/setup.py/blob/master/setup.py)
* [kennethreitz's blog post "A Better Pip Workflow"](https://www.kennethreitz.org/essays/a-better-pip-workflow)
* [Donald Stufft's blog post about setup.py vs requirements.txt](https://caremad.io/posts/2013/07/setup-vs-requirement/)
* [Kyle Knapp's talk @ PyCon 2018 "Automating Code Quality"](https://www.youtube.com/watch?v=G1lDk_WKXvY)
* [Hynek's blog post "Sharing Your Labor of Love: PyPI Quick and Dirty"](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/)
* Everyone writing blog posts/github issues/mailing list responses/twitter rants/etc about Python packaging, best practices, and development workflows
* All the wonderful folks writing the tools and services involved in this template and their documentation!
