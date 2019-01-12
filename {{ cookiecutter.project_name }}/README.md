{% set has_docs_folder = cookiecutter.create_docs_folder == 'y' -%}
{% set is_lib = cookiecutter.library_or_application == 'library' -%}
# {{cookiecutter.project_name}} [![v{{ cookiecutter.version }}](https://img.shields.io/badge/version-{{ cookiecutter.version }}-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/releases)

[![Build Status](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.svg?branch=master)](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}) [![Coverage Status](https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/badge.svg?branch=master)](https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}?branch=master){% if has_docs_folder %} [![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.github_repo_name }}/badge/?version=latest)](http://{{ cookiecutter.github_repo_name }}.readthedocs.io/en/latest/?badge=latest){% endif %}

{{ cookiecutter.short_description }}
{% if has_docs_folder %}
See the full documentation at https://{{cookiecutter.github_repo_name }}.readthedocs.io
{% endif %}
{% if is_lib %}
# Installation
- ```$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.slug_name }}.git```
- ```$ cd {{ cookiecutter.slug_name }}```
- ```$ python setup.py install```
{% else %}
# Installation
- ```$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.slug_name }}.git```
- ```$ cd {{ cookiecutter.slug_name }}```
- (Optional) Make any required changes to ```requirements.txt```
    - Note: Unpinning or changing dependency versions may effect functionality
- ```$ pip install -r requirements.txt```
- ```$ python setup.py install```
{% endif %}
# Development
## Running Tests
```
$ pip install -r requirements/requirements_tests.txt
$ tox
```
Note: Tox will run tests against the version of the software installed via ```python setup.py install```.
To test against pinned dependencies add ```-r requirements.txt``` to the deps array of the tox.ini testenv
section.

## Updating Dependencies
- ```pip install -r requirements/requirements_dev.txt```
- Review ```requirements/requirements_loose.txt```
- ```tox -e pindeps```
- ```cp .tox/requirements.txt .```
- Copy {% if is_lib %}minimally {% endif %}pinned requirements into ```setup.py```

# Author
{{ cookiecutter.author }} <{{ cookiecutter.email }}>
