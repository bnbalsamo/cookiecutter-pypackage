from setuptools import setup, find_packages


# Provided Package Metadata
NAME = "{{ cookiecutter.pip_name }}"
DESCRIPTION = "{{ cookiecutter.short_description }}"
VERSION = "{{ cookiecutter.version }}"
AUTHOR = "{{ cookiecutter.author }}"
AUTHOR_EMAIL = "{{ cookiecutter.email }}"
URL = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}'
PYTHON_REQUIRES= ">=3.6,<4"
INSTALL_REQUIRES = [
    # Put "abstract" / loosely pinned requirements here
    # See: https://caremad.io/posts/2013/07/setup-vs-requirement/
    # Ex:
    # 'requests'
]
EXTRAS_REQUIRE = {
    # Put "abstract" / loosely pinned requirements here
    # See: https://caremad.io/posts/2013/07/setup-vs-requirement/
    # Ex:
    # 'webfrontend': ['flask']
    "dev": [
        "bump2version",
        "invoke",
        "isort[pyproject] >= 5.0.2",
        "pylint >= 2.6.0",
        "black",
        "wheel",
        "build >= 0.2.1",
        "twine",
        "blacken-docs",
        "pip-tools",
    ],
    "tests": [
        "tox",
        "tox-pyenv",
        "pytest",
        "coverage[toml]",
        "pytest-cov",
    ],
    "docs": [
        "sphinx",
        "sphinx_rtd_theme",
    ]
}
ENTRY_POINTS = {
    # For CLI scripts, plugins, etc if required
    # Ex:
    # 'console_scripts': ['mycli=mymodule:cli'],
}


def readme():
    try:
        with open("README.md", 'r') as f:
            return f.read()
    except:
        return False


# Derived Package Metadata
LONG_DESCRIPTION = readme() or DESCRIPTION
if LONG_DESCRIPTION == DESCRIPTION:
    LONG_DESCRIPTION_CONTENT_TYPE = "text/plain"
else:
    LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"


# Set it up!
setup(
    name=NAME,
    description=DESCRIPTION,
    version=VERSION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    package_dir={"": "src"},
    packages=find_packages(
        where="src"
    ),
    entry_points=ENTRY_POINTS,
    include_package_data=True,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires=PYTHON_REQUIRES
)
