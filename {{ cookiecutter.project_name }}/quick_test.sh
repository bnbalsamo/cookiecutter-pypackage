#!/bin/sh
echo "==> Running Tests <=="
coverage run -m py.test \
    && echo "==> Coverage <==" && \
    coverage report
echo "==> Flake8 <=="
flake8
echo "==> isort <=="
isort -rc --diff -c {{ cookiecutter.slug_name }}
echo "If errors present, apply changes with isort -rc --atomic --apply {{ cookiecutter.slug_name }}"
echo "==> Bandit <== "
bandit -r {{ cookiecutter.slug_name }}
echo "==> Done <=="
