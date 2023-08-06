# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coloredmatrix']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'coloredmatrix',
    'version': '0.0.1',
    'description': 'ANSI color formatting for output in terminal',
    'long_description': '# Colored Console\n![GitHub](https://img.shields.io/github/license/JewinV/colored-console)',
    'author': 'Jewin Varghese',
    'author_email': 'jewinvarghese@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JewinV/coloredmatrix',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
