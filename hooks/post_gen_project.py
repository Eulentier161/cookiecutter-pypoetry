import os

os.system('cd "{{cookiecutter.project_name}}"')
os.system("poetry install")
os.system("git init")
os.system("git add .")
os.system('git commit -m "init"')
print("project build. 'cd {{cookiecutter.project_name}}' and hack away.")