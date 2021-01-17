# cookiecutter-pypackage [![v0.34.1](https://img.shields.io/badge/version-0.34.1-blue.svg)](https://github.com/bnbalsamo/cookiecutter-pypackage/releases)

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
- Testing via [tox](https://tox.readthedocs.io/en/latest/)
- CI via [GitHub Actions](https://github.com/features/actions)
- [CodeCov](https://codecov.io/) integration
- [pyup](https://pyup.io/) integration
- [Invoke](http://www.pyinvoke.org/) tasks to standardize development workflows, including...
    - Running the tests
    - Running autoformatters like black and isort
    - Easily checking `#TODO` comments
    - Building documentation
    - Pinning dependencies to a `requirements.txt`
    - Releasing to pypi
    - Building source distributions and wheels
    - Building wheelhouses of your project's dependencies
- A `README.md` that includes...
    - A brief project description
    - Installation instructions
    - relevant badges
    - Easy to follow directions for contributors
- (optional) [Sphinx](http://www.sphinx-doc.org) documentation
    - With a minimal autodocs setup
    - Ready for use with [readthedocs](https://readthedocs.org/)
- All the tooling you can shake a stick at, wrapped up in a ```tox``` config, properly configured to work together in harmony.
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
    - [mypy](http://mypy-lang.org/)
    - [interrogate](https://interrogate.readthedocs.io/en/latest/)


# Quickstart

- Requirements For These Instructions
    - [Cookiecutter](https://github.com/audreyr/cookiecutter)
    - [Github](https://github.com/) account
    - [CodeCov](https://codecov.io/) account
    - [readthedocs](https://readthedocs.org/) account
    - [pyup](https://pyup.io/) account
    - [pyenv](https://github.com/pyenv/pyenv)
    - [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
    - [xxenv-latest](https://github.com/momo-lab/xxenv-latest)
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
|github_default_branch_name|master (See [#45](https://github.com/bnbalsamo/cookiecutter-pypackage/issues/45))|Used for the CI badge and in the instructions for project bootstrapping|
|license|GNU GPLv3|The license to release the project under|
|create_docs_folder|y|Whether or not to create a separate docs folder for sphinx style documentation.|
|include_link_back_to_cookiecutter|y|Whether or not to include a link back this cookiecutter in the generated project's `README.md`|


# Preconfigured Invoke Tasks 

Any of the following can be run off the bat from the project root, via `invoke`/`inv`...

```
$ inv --list
Available tasks:

  pindeps                 Pin dependencies, creating or overwriting requirements.txt
  release                 Perform a release to pypi.
  build.coverage-report   Build an HTML coverage report.
  build.dists             Build distribution artifacts.
  build.docs              Build the documentation.
  build.wheelhouse        Build a dependency wheelhouse.
  check.todos             Check for `#TODO` comments in the code.
  clean.all               Remove all clean-able artifacts.
  clean.compiled          Remove compilation artifacts.
  clean.coverage          Remove the .coverage cache.
  clean.coverage-report   Remove the html coverage report.
  clean.dists             Remove existing distributions.
  clean.docs              Remove existing docs.
  clean.mypy              Remove the .mypy_cache directory.
  clean.tox               Remove the .tox cache directory.
  clean.wheelhouse        Remove the wheelhouse.
  run.autoformatters      Run all the autoformatters.
  run.black               Run `black` to autoformat the source code.
  run.blacken-docs        Run `blacken-docs` to autoformat code in the documentation.
  run.isort               Run `isort` to autoformat the source code.
  run.tests               Run the tests.
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

**It uses requirements.txt rather than Pipfile and Pipfile.lock**

I made this decision because the pipfile specification isn't integrated into pip (yet),
because it allows for fewer differences between developing applications and libraries,
and because I don't particularly like the fact that the existing tools attempt
to be a "one stop shop" for managing dependency declarations and virtualenvs.

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

The python ecosystem includes _a ton_ of useful tooling, but remembering the names, options,
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
* Everyone writing blog posts/github issues/mailing list responses/twitter rants/etc about Python packaging, best practices, and development workflows
* All the wonderful folks writing the tools and services involved in this template and their documentation!
