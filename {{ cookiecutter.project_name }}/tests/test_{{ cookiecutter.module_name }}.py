"""Tests for {{ cookiecutter.module_name }}."""

import pytest

import {{ cookiecutter.module_name }}


def test_version_available() -> None:
    """Test that the module has a version dunder."""
    assert hasattr({{ cookiecutter.module_name }}, "__version__")


if __name__ == "__main__":
    pytest.main([__file__])
