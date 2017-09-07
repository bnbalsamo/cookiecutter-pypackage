from setuptools import setup, find_packages


def readme():
    with open("README.md", 'r') as f:
        return f.read()


setup(
    name="{{ cookiecutter.slug_name }}",
    description="{{ cookiecutter.short_description }}",
    version="{{ cookiecutter.version }}",
    long_description=readme(),
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    packages=find_packages(
        exclude=[
        ]
    ),
    include_package_data=True,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.slug_name }}',
    install_requires=[
    ],
    tests_require=[
        'pytest'
    ],
    test_suite='tests'
)
