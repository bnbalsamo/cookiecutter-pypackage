"""Tests for {{ cookiecutter.project_name }}."""
import pytest

import {{ cookiecutter.module_name }}


def test_version_available() -> None:
    """Test the version dunder is available on the module."""
    version_attr = getattr({{ cookiecutter.module_name }}, "__version__", None)
    assert version_attr is not None


if __name__ == "__main__":
    pytest.main()
