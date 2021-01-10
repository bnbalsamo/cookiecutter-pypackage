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
- ```$ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name }}.git```
- ```$ cd {{ cookiecutter.github_repo_name }}```
    - If you would like to install the pinned dependencies, run ```pip install -r requirements.txt```
- ```$ python -m pip install .```

# Development

## Quickstart

To quickly install + configure a development environment...

Install [pyenv](https://github.com/pyenv/pyenv), [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv),
and [xxenv-latest](https://github.com/momo-lab/xxenv-latest) and copy the following into your terminal while
in the repository root.

```bash
[[ `type -t pyenv` ]] && \
[ -s "$PYENV_ROOT/plugins/pyenv-virtualenv" ] && \
[ -s "$PYENV_ROOT/plugins/xxenv-latest" ] && \
pyenv latest install -s 3.8 && \
PYENV_LATEST_38=$(pyenv latest -p 3.8) && \
pyenv latest install -s 3.7 && \
PYENV_LATEST_37=$(pyenv latest -p 3.7) && \
pyenv latest install -s 3.6 && \
PYENV_LATEST_36=$(pyenv latest -p 3.6) && \
pyenv virtualenv "$PYENV_LATEST_38" "{{ cookiecutter.project_name }}" && \
pyenv local "{{ cookiecutter.project_name }}" "$PYENV_LATEST_38" "$PYENV_LATEST_37" "$PYENV_LATEST_36" && \
pip install -e .[dev,tests,docs]
```

## Manual Configuration

If you choose not to use the quickstart script you will need to...

- Create a virtual environment
- Install the development dependencies
    - `pip install -e .[dev,tests,docs]`
- Configure tox so that it can access all relevant python interpreters

## Running Tests
```
$ inv run.tests
```

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

_Created using [bnbalsamo/cookiecutter-pypackage](https://github.com/bnbalsamo/cookiecutter-pypackage) v0.33.2_
{% endif -%}
