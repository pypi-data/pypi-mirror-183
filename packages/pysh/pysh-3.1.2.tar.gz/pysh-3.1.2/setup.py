# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysh']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pysh',
    'version': '3.1.2',
    'description': 'A library of small functions that simplify scripting in python',
    'long_description': '# pysh\n\nA library of small functions that simplify scripting in python\n\n## Installation\n\n```bash\npip install pysh\n```\n\n## Usage\n\n```python\nfrom pysh import sh, cd, env, which\n\nsh("git status") # will display the output of git status\nres = sh("git status", capture=True) # will capture stdout and stderr of git status\nprint(res.stdout) # will print stdout of git status\n\n\ncd("path/to/dir") # will change the current working directory to path/to/dir\nwith cd("path/to/dir"): # will change the current working directory to path/to/dir and then change it back to the original directory\n    sh("git status")\n\n\nenv(var="value") # will set the environment variable var to value\nwith env(PGPASSWORD="MyPassword"): # will set the environment variable PGPASSWORD to MyPassword and then set it back to the original value\n    sh("createdb -U postgres -h localhost -p 5432 -O postgres mydb")\n\n\nwhich("git") # will return the path to the git executable or None if git is not installed\n\n```\n',
    'author': 'Stanislav Zmiev',
    'author_email': 'szmiev2000@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Ovsyanka83/pysh',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
