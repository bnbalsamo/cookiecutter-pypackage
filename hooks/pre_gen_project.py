import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'


project_name = '{{ cookiecutter.project_name }}'
module_name = '{{ cookiecutter.module_name}}'


# Check project name
if re.match(r'\s', project_name):
    print('ERROR: The project_name (%s) can not contain whitespace.' % project_name)
    sys.exit(1)


# Check module name
if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The module_name (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)

    # Exit to cancel project
    sys.exit(1)
