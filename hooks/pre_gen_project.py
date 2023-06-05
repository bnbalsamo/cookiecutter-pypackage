"""
Pre generation script.

Template variables in this script will be substituted before execution.

Exiting non-zero from this script will halt template rendering.
"""

import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"


project_name = "{{ cookiecutter.project_name }}"
module_name = "{{ cookiecutter.module_name}}"


# Check project name
if re.match(r"\s", project_name):
    print("ERROR: The project_name (%s) can not contain whitespace." % project_name)
    sys.exit(1)


# Check module name
if not re.match(MODULE_REGEX, module_name):
    print(
        "ERROR: The module_name (%s) is not a valid Python module name." % module_name
    )
    sys.exit(1)
