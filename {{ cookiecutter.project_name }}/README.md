{% set has_docs_folder = cookiecutter.create_docs_folder == 'y' -%}
{% set include_link_back = cookiecutter.include_link_back_to_cookiecutter == 'y' -%}
# {{cookiecutter.project_name}} [![v{{ cookiecutter.version }}](https://img.shields.io/badge/version-{{ cookiecutter.version }}-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/releases)

[![CI](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/workflows/CI/badge.svg?branch={{ cookiecutter.github_default_branch_name }})](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/actions)
[![Coverage](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/)
{% if has_docs_folder %} [![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.github_repo_name }}/badge/?version=latest)](http://{{ cookiecutter.github_repo_name }}.readthedocs.io/en/latest/?badge=latest) {% endif %}
[![Updates](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

{{ cookiecutter.short_description }}
{% if has_docs_folder %}
See the full documentation at https://{{cookiecutter.github_repo_name }}.readthedocs.io
{% endif %}
# Installation
- ```$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.slug_name }}.git```
- ```$ cd {{ cookiecutter.slug_name }}```
    - If you would like to install the pinned dependencies, run ```pip install -r requirements.txt```
- ```$ python setup.py install```

# Development

## Installing Development Dependencies
```
$ pip install -r requirements/requirements_dev.txt
```

## Running Tests
```
$ inv run.tests
```
Note: Tox will run tests against the version of the software installed via ```python setup.py install```.

## Running autoformatters
```
$ inv run.autoformatters
```

## Pinning Dependencies
```
$ inv pindeps
```

# Author
{{ cookiecutter.author }} <{{ cookiecutter.email }}>

{%- if include_link_back %}

_Created using [bnbalsamo/cookiecutter-pypackage](https://github.com/bnbalsamo/cookiecutter-pypackage) v0.27.0_
{% endif -%}
