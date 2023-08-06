# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dir2path']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['dir2path = dir2path.console:run']}

setup_kwargs = {
    'name': 'dir2path',
    'version': '0.1.0',
    'description': 'Add current directory to your PATH',
    'long_description': '# Dir2Path\n\n`dir2path` is a simple utility that appends the current directory to your shells `$PATH`. Currently supports ZSH and BASH.\n\n## Installation\n\ninstallation via pip\n\n```shell\n$ pip install dir2path\n```\n\n## Usage\n\n```shell\n$ cd ~/my/local/bin/folder\n$ dir2path\n```\n',
    'author': 'Josh Burns',
    'author_email': 'joshyburnss@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
