# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pinit']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pinit',
    'version': '0.0.0',
    'description': 'an application for creating shortcut for apps and scripts in linux',
    'long_description': '',
    'author': 'ramin',
    'author_email': 'ramin.kishani.farahani@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
