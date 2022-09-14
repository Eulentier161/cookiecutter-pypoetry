import re
import sys

project_name = "{{cookiecutter.project_name}}"
PROJECT_NAME_REGEX = r"^[a-z][-_a-z0-9]+$"
if not re.match(PROJECT_NAME_REGEX, project_name):
    print("project_name has to match /^[a-z][-_a-z0-9]+$/")
    sys.exit(1)

module_name = "{{cookiecutter.module_name}}"
MODULE_NAME_REGEX = r"^[a-z][_a-z0-9]+$"
if not re.match(MODULE_NAME_REGEX, module_name):
    print("module_name has to match /^[a-z][_a-z0-9]+$/")
    sys.exit(1)