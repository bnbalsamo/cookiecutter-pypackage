{% set include_link_back = cookiecutter.include_link_back_to_cookiecutter == 'y' -%}
# {{cookiecutter.project_name}} [![v{{ cookiecutter.version }}](https://img.shields.io/badge/version-{{ cookiecutter.version }}-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/releases)

[![CI](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/workflows/CI/badge.svg?branch={{ cookiecutter.github_default_branch_name }})](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/actions)
[![Coverage](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/branch/{{ cookiecutter.github_default_branch_name }}/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/)
[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.github_repo_name }}/badge/?version=latest)](http://{{ cookiecutter.github_repo_name }}.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/shield.svg)](https://pyup.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

{{ cookiecutter.short_description }}

See the full documentation at https://{{cookiecutter.github_repo_name }}.readthedocs.io

# Installation

This project is currently only installable via development tooling.

- Install [poetry](https://python-poetry.org/)
- ```$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.git```
- ```$ cd {{ cookiecutter.github_repo_name }}```
- ```$ poetry install --no-dev```

# Development

To install + configure a development environment...

- Install [poetry](https://python-poetry.org/)
- Clone the repository
    - `git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.git`
- `cd` into the project directory
    - `cd {{ cookiecutter.github_repo_name }}`
- Install the project and development dependencies with poetry
    - `poetry install -E docs -E tests`
- Activate the project's virtual environment in your current shell
    - `poetry shell`
- Install the pre-commit hooks
    - `pre-commit install --install-hooks`

Development tasks are available via the `tasks.py` [invoke](http://www.pyinvoke.org/)
script. After installation you can view the help via `inv --list`

## Running Tests
```
$ inv run.tests
```

## Running autoformatters
```
$ inv run.autoformatters
```

## Upgrading Dependencies
```
$ poetry update
```

# Author
{{ cookiecutter.author }} <{{ cookiecutter.email }}>

{%- if include_link_back %}

_Created using [bnbalsamo/cookiecutter-pypackage](https://github.com/bnbalsamo/cookiecutter-pypackage) v0.44.1_
{% endif -%}
