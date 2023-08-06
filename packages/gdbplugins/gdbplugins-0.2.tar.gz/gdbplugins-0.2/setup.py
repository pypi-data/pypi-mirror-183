# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gdbplugins']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['deploy_gdbplugins_loader = gdbplugins.deploy:main'],
 'gdbplugins.plugins': ['python-plugin = gdbplugins.python:main',
                        'ruby-plugin = gdbplugins.ruby:main']}

setup_kwargs = {
    'name': 'gdbplugins',
    'version': '0.2',
    'description': 'Python plugins for gdb making debugging various languages with gdb easy.',
    'long_description': '# The gdbplugins.\n\n[![.github/workflows/main.yml](https://github.com/jarovo/gdbplugins/actions/workflows/main.yml/badge.svg)](https://github.com/jarovo/gdbplugins/actions/workflows/main.yml)\n\nPython plugins for gdb making debugging various languages with gdb easy.\n\n\n## Installation\n\nOn RHEL and Fedora, this will make it happen system-wide:\n\n    sudo pip install --prefix / gdbplugins\n\nNote that to install, we cannot use virtualenv as gdb does not load the virtualenv.\n\nNext time you start gdb, the plugins should load.\n',
    'author': 'Jaroslav Henner',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
