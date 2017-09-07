#!/bin/sh
echo "==> Running Tests <=="
coverage run --source {{ cookiecutter.slug_name }} -m py.test \
    && echo "==> Coverage <==" && \
    coverage report
echo "==> Flake8 <=="
flake8
echo "==> Done <=="
