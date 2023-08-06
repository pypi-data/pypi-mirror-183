# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['copy_progress']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['copy-progress = copy_progress.copy:main']}

setup_kwargs = {
    'name': 'copy-progress',
    'version': '0.1.3',
    'description': 'Copy files or directories to a new location with progress bars for each item.',
    'long_description': '# copy-progress\n \nThis tool allows you to copy files or directories to a new location with progress bars for each item.',
    'author': 'Caelan Barondess',
    'author_email': 'cbarondess19@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/cbarond/copy-progress',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
