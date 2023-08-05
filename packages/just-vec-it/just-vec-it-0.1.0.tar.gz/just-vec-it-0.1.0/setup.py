# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['just_vec_it']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'just-vec-it',
    'version': '0.1.0',
    'description': 'part of my personal software ecosystem',
    'long_description': None,
    'author': 'Andrew Matte',
    'author_email': 'andrew.matte@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
