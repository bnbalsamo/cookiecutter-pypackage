# cookiecutter-pypackage

My [cookiecutter](https://github.com/audreyr/cookiecutter) template for python packages.

## Quick Start

- Install [cruft](https://cruft.github.io/cruft/) via [`pipx`](https://pypa.github.io/pipx/)
    - `$ pipx install cruft`
- Create a GitHub repository
- Add a [PyPI API token](https://pypi.org/manage/account/) to the repository secrets (for releases via GitHub Actions)
    - Navigate the repository `Settings` page
    - Expand the `Secrets and variables` subsection of the `Security` settings section
    - Click `Actions`
    - Add a new `Repository secret` named `PYPI_TOKEN` that contains your PyPI API token
- Use cruft to render the template
    - Be sure the `project_name` variable matches the name of your github repository!
    - `$ cruft create https://github.com/bnbalsamo/cookiecutter-pypackage`
- Follow the bootstrapping instructions printed to the terminal after the template is rendered
- Make any changes to the template you'd like (licenses, README formatting, etc)
- Begin Developing!

## Whats it Get Me?

- A modern python project setup including...
    - a `src/` layout
    - declarative configuration in `pyproject.toml`
    - full support for modern build standards (rendered projects use [`flit`](https://flit.pypa.io/en/stable/) and are built via [`build`](https://pypa-build.readthedocs.io/en/latest/))
- [`invoke`](https://www.pyinvoke.org/) tasks for facilitating local development and wrapping all other tools into one easy to use CLI
- Pre-configured testing and linting powered by [`nox`](https://nox.thea.codes/en/stable/) and [`pre-commit`](https://pre-commit.com/)
    - unit testing and coverage metrics via [`pytest`](https://docs.pytest.org/en/latest/) and [`coverage.py`](https://coverage.readthedocs.io/en/7.2.7/)
    - type checking via [`mypy`](https://mypy.readthedocs.io/en/latest/)
    - linting via [`ruff`](https://beta.ruff.rs/docs/) and [`pylint`](https://pylint.readthedocs.io/en/latest/)
    - code formatting via [`black`](https://black.readthedocs.io/en/stable/) and [`ruff`](https://beta.ruff.rs/docs/)
    - docstring coverage via [`interrogate`](https://interrogate.readthedocs.io/en/latest/)
- CI via [Github Actions](https://github.com/features/actions)
    - Including partially automated releasing to [PyPI](https://pypi.org/)
- Documentation built via [MkDocs](https://www.mkdocs.org/) hosted on [GitHub Pages](https://pages.github.com/)
- Changelog auto generation via [`towncrier`](https://towncrier.readthedocs.io/en/stable/)
- Version management via [`bumpver`](https://github.com/mbarkhau/bumpver)
- A prepopulated `README.md` that includes documentation for project development and contributing
- GitHub templates for [Issues](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository) and [Pull Requests](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
- A [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) configuration
- An [editorconfig](https://editorconfig.org/) configuration
- A variety of other tooling configured to work together in harmony to keep your project's code quality high and make contributing easy

## Cookiecutter Parameters

|Parameter Name|Default|Description|
|--------------|-------|-----------|
|project_name|n/a|The name of the project. Used for display purposes and as the name of the containing directory and the GitHub repository. Should not contain whitespace.|
|pip_name|`$project_name.lower().replace(' ', '-')`|The "pip name" of the project. This name will appear in commands like `pip freeze` and (if the project is published on pypi) this name will be used in commands like `pip install`|
|module_name|`$project_name.lower().replace(' ', '_').replace('-', '_')`|The name of the actual python module, eg: what is used in `import` statements.|
|version|`1000.1`|The version to initialize the project at. This version number should parsable by [bumpver](https://pypi.org/project/bumpver/) as configured in the `pyproject.toml`.|
|short_description|`A package.`|A one line description of your project for use in documentation.|
|author|`First Last`|Included in the project metadata.|
|email|`you@provider.com`|Included in the project metadata.|
|github_repo_name|`$project_name`|Used to derive the github URL of the project.|
|github_username|`github_username`|Used to derive the github URL of the project.|
