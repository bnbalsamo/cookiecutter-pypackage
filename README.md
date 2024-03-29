# cookiecutter-pypackage [![v0.48.0](https://img.shields.io/badge/version-0.48.0-blue.svg)](https://github.com/bnbalsamo/cookiecutter-pypackage/releases)

[![CI](https://github.com/bnbalsamo/cookiecutter-pypackage/workflows/CI/badge.svg?branch=master)](https://github.com/bnbalsamo/cookiecutter-pypackage/actions)

My [cookiecutter](https://github.com/audreyr/cookiecutter) template for python packages

[See an example of a generated project here](https://github.com/bnbalsamo/bnb-cookiecutter-example/)


# Table of Contents

- [Whats it get me?](#whats-it-get-me)
- [Quickstart](#quickstart)
- [Cookiecutter Parameters](#cookiecutter-parameters)
- [Preconfigured Invoke Tasks](#preconfigured-invoke-tasks)
- [Uploading to Pypi](#uploading-to-pypi)
- [Opinions](#opinions)
- [Credit Where It's Due](#credit-where-its-due)


# Whats it get me?

tl;dr: A CI enabled Python software project with plenty of bells and whistles.

- [GitHub](https://github.com/) integration
- Testing via [nox](https://nox.thea.codes/en/stable/) and [pre-commit](https://pre-commit.com/)
- CI via [GitHub Actions](https://github.com/features/actions)
- [CodeCov](https://codecov.io/) integration
- [pyup](https://pyup.io/) integration
- [Invoke](http://www.pyinvoke.org/) tasks to standardize development workflows, including...
    - Running the tests
    - Running autoformatters like [black](https://github.com/ambv/black)
    and [isort](https://github.com/timothycrosley/isort)
    - Easily checking `#TODO` comments
    - Building documentation
    - Serving documentation locally during development
    - Managing dependencies precisely and securely with [poetry](https://python-poetry.org/)
    - Releasing to [pypi](https://pypi.org/)
    - Building source distributions and wheels
    - Building self-contained zipapps via [shiv](https://shiv.readthedocs.io/en/latest/)
    - Cleaning up your development environment
- A `README.md` that includes...
    - A brief project description
    - Installation instructions
    - relevant badges
    - Easy to follow directions for contributors
- [Sphinx](http://www.sphinx-doc.org) documentation
    - Ready for use with [readthedocs](https://readthedocs.org/)
    - Preconfigured with several staple sphinx extensions
        - [autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
        - [intersphinx](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html)
        - [todo](https://www.sphinx-doc.org/en/master/usage/extensions/todo.html)
        - [sphinx-autodoc-typehints](https://pypi.org/project/sphinx-autodoc-typehints/)
- All the tooling you can shake a stick at, wrapped up in a ```nox``` config, properly configured to work together in harmony.
    - [pytest](https://docs.pytest.org/en/latest/)
    - [flake8](http://flake8.pycqa.org/en/latest/)
    - [pylint](https://www.pylint.org)
    - [coverage](https://coverage.readthedocs.io/en/latest/)
    - [check-manifest](https://github.com/mgedmin/check-manifest)
    - [isort](https://github.com/timothycrosley/isort)
    - [bandit](https://github.com/PyCQA/bandit)
    - [pydocstyle](www.pydocstyle.org/en/latest/)
    - [safety](https://pyup.io/docs/safety/installation-and-usage/)
    - [black](https://github.com/ambv/black)
    - [blacken-docs](https://github.com/asottile/blacken-docs)
    - [mypy](http://mypy-lang.org/)
    - [interrogate](https://interrogate.readthedocs.io/en/latest/)
    - [sphinx linkcheck](https://www.sphinx-doc.org/en/master/usage/builders/index.html#sphinx.builders.linkcheck.CheckExternalLinksBuilder)
    - [build](https://pypi.org/project/build/) a PEP517 package builder
- Some extra goodies for your development environment like...
    - A preconfigured [editorconfig](https://editorconfig.org/) file.
    - A preconfigured [bump2version](https://pypi.org/project/bump2version/) configuration file.


# Quickstart

- Requirements For These Instructions
    - [Cookiecutter](https://github.com/audreyr/cookiecutter)
    - [Github](https://github.com/) account
        - [With SSH access configured](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
    - [CodeCov](https://codecov.io/) account
    - [readthedocs](https://readthedocs.org/) account
    - [pyup](https://pyup.io/) account
    - [poetry](https://python-poetry.org)
- Steps
    - Create a github repo named $YOUR_PROJECT_NAME
    - Enable repository monitoring on readthedocs
    - Enable repository monitoring in pyup
    - ```$ cookiecutter gh:bnbalsamo/cookiecutter-pypackage```
    - Fill in the prompts
    - Complete the setup instructions printed in your terminal after template rendering
    - Begin developing your package!


# Cookiecutter Parameters

|Parameter Name|Default|Description|
|--------------|-------|-----------|
|project_name|n/a|The name of the project. Used for display purposes and as the name of the containing directory and the GitHub repo. Should not contain whitespace.|
|pip_name|$project_name.lower()|The "pip name" of the project. This name will appear in commands like `pip freeze` and (if the project is published on pypi) this name will be used in commands like `pip install`|
|module_name|$project_name.lower().replace("-","_")|The name of the actual python module, eg: what is used in `import` statements.|
|version|0.0.1|The version to initialize the project at. This version number should parsable by [bump2version](https://github.com/c4urself/bump2version)|
|short_description|A project.|A one line description of your project for use in documentation.|
|author|First Last|The name of the author of the software. Used in documentation and the `__author__` dunder on your package.|
|email|you@provider.com|Included in the `README.md`, used as the contact email for your pypi package, and included in the package's `__email__` dunder.|
|github_repo_name|$project_name|Used to derive the github URL of the project|
|github_username|githubber|Used to derive the github URL of the project|
|github_default_branch_name|main|Used for the CI badge and in the instructions for project bootstrapping|
|license|GNU GPLv3|The license to release the project under|
|enforce_strong_typing|n|If set to `y` mypy will error on untyped defs.|
|include_link_back_to_cookiecutter|y|If set to `y`the generated project's `README.md` will include a link back this cookiecutter.|


# Preconfigured Invoke Tasks

Any of the following can be run off the bat from the project root, via `invoke`/`inv`...

```
$ inv --list
=> Current Working Directory: ...
Available tasks:

  clean                   Clean up all caches and generated artifacts.
  format                  Run all the formatters.
  lint                    Run pre-commit against all files.
  release                 Perform a release to pypi.
  test                    Run the tests.
  build.coverage-report   Build an HTML coverage report.
  build.dists (build)     Build distribution artifacts.
  build.docs              Build the documentation.
  build.zipapp            Use `shiv` to produce a zipapp that includes the dependencies.
  check.todos             Check for `#TODO` comments in the code.
  serve.docs              Serve the docs on localhost:8000. Reload on changes.
```

Additional information about commands can be obtained by using their `--help` flag, eg:

```
$ inv release --help
Usage: inv[oke] [--core-opts] release [--options] [other tasks here ...]

Docstring:
  Perform a release to pypi.

Options:
  -b, --[no-]build
  -c, --[no-]clean
  -p, --prod
  -s, --skip-tests
```


## Uploading to pypi

Review your package before publishing it!

[This](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/) blog
entry provides a good breakdown of uploading a package to pypi.

The commands required to release are provided as an `invoke` task:

```
$ inv release --prod  # Omit the --prod flag to publish to test.pypi
```


# Opinions

This template is opinionated (aren't they all, really?) in a couple of ways.

**It keeps all of the static analysis tooling dialed up _fairly_ strictly.**

This isn't meant to imply that every project should keep the static analysis tooling
dialed up so strictly, but rather that if you are loosening controls on your static analysis
for a good reason that reason should be documented as a part of your codebase's git history.
This helps keep relevant decisions documented with the code.

**It causes testing to fail below 80% code coverage.**

80% is arbitrary, but I've found it works fairly well for me when starting a project. If while
I'm actively developing and the code base is small I fall below 80% coverage I know I've
probably slacked off on tests somewhere. As a codebase grows and matures I tend to turn this
metric up to whatever reasonable maximum I can hit.

**It uses [poetry](https://python-poetry.org/).**

Packaging in the larger Python ecosystem is currently undergoing some significant
changes, and several tools (or combinations of tools) exist to handle packaging,
dependency management, environment management, artifact generation, uploading to
package indices, etc.

Poetry provides a couple of key functionalities:

- A solver which maps dependency constraints to a working combination of dependency
  versions
- The ability to have (regular) dependencies, development dependencies, and extras.
- A lock file, to provide deterministic environment creation, that contains hashes
- The ability to export a `pip`-compatible constraints file, that can be used
  to create environments which contain subsets of dependencies for testing.
- The ability to store all metadata in `pyproject.toml`

These functionalities, in combination with the fact that they require almost no custom code
(ecept the `install_with_constraints` function in the noxfile), make `poetry` my tool of
choice for packaging, currently.

**It implements a lot of tooling.**

Well, thats the whole reason for the use of a cookiecutter, isn't it? I'm of the opinion
that even if a project chooses not use every tool in this template, it's easier to rip out
a few pieces here and there than it is to properly re-implement them. Thus I've tended to err
on the side of including tooling, rather than omitting it.

**It uses web service X instead of competing service Y.**

My choice of services is informed by:
- What services I'm comfortable with implementing
- What services appear to be popular within the python community

If the services this repository implement are (significantly) eclipsed by similar services
in the future open an issue and let me know!

**It uses [semver](https://semver.org/) for versioning.**

I'm of the opinion that semver is applicable to the vast majority of projects. If, for whatever
reason, it isn't applicable to a given project, changing the versioning scheme along with the
justification should be included in the git history.

**It uses a "src" layout**

I've [been](https://hynek.me/articles/testing-packaging/) [convinced](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure).

**It uses [invoke](http://www.pyinvoke.org/) as a task runner.**

The Python ecosystem includes _a ton_ of useful tooling, but remembering the names, options,
and flags for every individual command, as well as implementing consistent workflows involving
all of them can be a chore.

Invoke provides (in my opinion) a clean, extensible, understandable method for effectively
utilizing all of these diverse tools, implementing repeatable workflows, and communicating
usage information to contributors.



# Credit Where It's Due

Inspiration (and some code) taken from the following:
* [audreyr's pypackage template](https://github.com/audreyr/cookiecutter-pypackage)
* [kennethreitz setup.py template](https://github.com/kennethreitz/setup.py/blob/master/setup.py)
* [kennethreitz's blog post "A Better Pip Workflow"](https://www.kennethreitz.org/essays/a-better-pip-workflow)
* [Donald Stufft's blog post about setup.py vs requirements.txt](https://caremad.io/posts/2013/07/setup-vs-requirement/)
* [Kyle Knapp's talk @ PyCon 2018 "Automating Code Quality"](https://www.youtube.com/watch?v=G1lDk_WKXvY)
* [Hynek's blog post "Sharing Your Labor of Love: PyPI Quick and Dirty"](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/)
* [Hynek's blog post "Python in GitHub Actions](https://hynek.me/articles/python-github-actions/)
* [Kyle Knapp's talk @ PyGotham 2018 "Automating Code Quality: Next Level](https://www.youtube.com/watch?v=iKAaNaVpJFM)
* [Thea Flowers' talk @ PyCon 2019 "Break the Cycle: Three excellent Python tools to automate repetitive tasks"](https://www.youtube.com/watch?v=-BHverY7IwU)
* [Daniele Procida's Diátaxis Documentation Framework](https://diataxis.fr/)
* Everyone writing blog posts/github issues/mailing list responses/twitter rants/etc about Python packaging, best practices, and development workflows
* All the wonderful folks writing the tools and services involved in this template and their documentation!
