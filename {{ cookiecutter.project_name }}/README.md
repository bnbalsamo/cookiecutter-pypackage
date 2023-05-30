# {{ cookiecutter.project_name }}

{{ cookiecutter.short_description}}

[Check out the documentation for more information.](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_name }})

## Contributing

### Development

To set up your development environment ensure you have python 3.8+ installed and run...

```
$ git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo_name}}.git
$ cd {{ cookiecutter.github_repo_name }}
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements/dev_requirements.txt
$ python -m invoke install
$ python -m pre_commit install --install-hooks
```

After setting up your development environment run the tests to confirm your environment operates correctly:

```
$ python -m invoke test
```

Note: Rather than using `python -m invoke` you may choose to use the shorter `invoke` or `inv` command.
These instructions use the `python -m` syntax to avoid any issues with global `invoke` installations/path variables/python paths.

Alternatively, this project supports a [VSCode dev container](https://code.visualstudio.com/docs/devcontainers/containers).

_Created using [bnbalsamo/cookiecutter-pypackage](https://github.com/bnbalsamo/cookiecutter-pypackage)_
