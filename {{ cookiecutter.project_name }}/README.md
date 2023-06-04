# {{ cookiecutter.project_name }}

{{ cookiecutter.short_description}}

[Check out the documentation for more information.](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.github_repo_name }})

## Contributing

### Issues/Bug Reports/Feature Requests

Please use the [github issues interface](https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.github_repo_name }}/issues) to report bugs or request features.

Click `New issue`, select the template that best fits your issue, and fill out the issue template to the best of your ability.

### Pull Requests

If no issue exists referencing what your PR intends to do please create an issue first.

See the "Development Environment Configuration" section of the `README.md` for details on configuring a local development environment.

Please create a newsfragment in `./newsfragments` as part of your pull request.

When ready for review please fill out the pull request template to the best of your ability and follow the included instructions.

## Development

### Development Environment Configuration

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

### Development Tasks (testing, linting, etc)

Common development tasks are wrapped via `invoke` tasks and defined in `tasks.py`.

Once your development environment is configured run `inv --list` for a list of available commands.

For more information on any command run `inv --help <command>`

### Releasing

Run `inv prepare` to update the change log and create a release tag.

On the GitHub Web UI for the repo click `Releases` -> `Draft a new release`

Select the tag that `inv prepare` created, make the release title the same as the tag, and click `Publish release`

CI does the rest!

### Adding Dependencies

Runtime dependencies should be added in `pyproject.toml`

Documentation, testing, or development dependencies should be added to the appropriate `*requirements.txt` file in the `./requirements` directory.

---

_Created using [bnbalsamo/cookiecutter-pypackage](https://github.com/bnbalsamo/cookiecutter-pypackage)_
