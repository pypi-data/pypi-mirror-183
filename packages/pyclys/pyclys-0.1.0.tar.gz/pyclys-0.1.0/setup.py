# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyclys']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyclys',
    'version': '0.1.0',
    'description': 'a simples clear dm',
    'long_description': '',
    'author': 'SundayC-137',
    'author_email': 'nicolas.lopesbis@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
