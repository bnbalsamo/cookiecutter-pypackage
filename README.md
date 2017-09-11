# cookiecutter-pypackage

v0.1.0

[![Build Status](https://travis-ci.org/bnbalsamo/cookiecutter-pypackage.svg?branch=master)](https://travis-ci.org/bnbalsamo/cookiecutter-pypackage)

My cookiecutter template for python packages

# Whats it get me?
- [Github](https://github.com/) integration
- [TravisCI](https://travis-ci.org/) integration
- [Coveralls](https://coveralls.io/) integration
- A minimal README
- Packages for common development tasks
    - [pip](https://pip.pypa.io/en/latest/)
    - [bumpversion](https://github.com/peritus/bumpversion)
    - [wheel](http://pythonwheels.com/)
    - [flake8](http://flake8.pycqa.org/en/latest/)
    - [coverage](https://coverage.readthedocs.io/en/coverage-4.4.1/)
    - [pytest](https://docs.pytest.org/en/latest/)
    - [twine](https://pypi.python.org/pypi/twine)

# Quickstart

- Requirements For These Instructions
    - [virtualenv](https://virtualenv.pypa.io/en/stable/)
    - [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
        - Properly configured for Project Management
    - [Github](https://github.com/) account
    - [TravisCI](https://travis-ci.org/) account
    - [Coveralls](https://coveralls.io/) account
- Steps
    - Create a github repo named $YOUR_PROJECT_NAME
    - Enable repository monitoring on Travis
    - Enable repository monitoring on coveralls
    - ```$ mkproject $YOUR_PROJECT_NAME```
    - ```$ pip install cookiecutter```
    - ```$ cookiecutter gh:https://github.com/bnbalsamo/cookiecutter-pypackage.git```
    - Fill in the prompts, be sure $YOUR_PROJECT_NAME matches the Github repository name
    - ```$ cd $YOUR_PROJECT_NAME```
    - ```$ git init```
    - ```$ git add *```
    - ```$ git commit -m "first commit"```
    - ```$ git remote add origin $YOUR_REPO_ADDRESS```
    - ```$ git push```
    - ```pip install -r requirements_dev.txt```
    - Begin developing your package!

# Functionalities

Any of the following can be run off the bat from the project root

* ```./quick_test.sh```: Run tests, generate coverage stats, run flake8
* ```py.test```: Run tests
* ```bumpversion $PART```: Bump the version number of the project
    * ```git push && git push --tags``` to upload/release to git
* ```autopep8 .```: Automatically fix some pep8 errors
* ``` check-manifest .```: Check that your manifest file is correct
    * the ```-c``` option will create one, if it doesn't exist
    * the ```-u``` option will update an existing file, or create one

## Uploading to pypi

I'll not hazard a short answer here, as there are too many options.

[This](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/) blog
entry provides a good breakdown of uploading a package to pypi. All of the referenced
tools should be installed by a ```pip -r requirements_dev.txt``` in your project
virtualenv.

Inspiration (and some code) taken from [audreyr's pypackage template](https://github.com/audreyr/cookiecutter-pypackage)
