"""Tests for {{ cookiecutter.project_name }}."""
import pytest

import {{ cookiecutter.module_name }}


def test_version_available():
    """Test the version dunder is available on the module."""
    x = getattr({{ cookiecutter.module_name }}, "__version__", None)
    assert x is not None


if __name__ == "__main__":
    pytest.main()
