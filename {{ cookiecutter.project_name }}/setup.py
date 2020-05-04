from setuptools import setup, find_packages


# Provided Package Metadata
NAME = "{{ cookiecutter.slug_name }}"
DESCRIPTION = "{{ cookiecutter.short_description }}"
VERSION = "{{ cookiecutter.version }}"
AUTHOR = "{{ cookiecutter.author }}"
AUTHOR_EMAIL = "{{ cookiecutter.email }}"
URL = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.slug_name }}'
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
    # 'webfrontend': {'flask'}
}
ENTRY_POINTS = {
    # For CLI Scripts, if required
    # Ex:
    # 'console_scripts': ['mycli=mymodule:cli'],
	#
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
