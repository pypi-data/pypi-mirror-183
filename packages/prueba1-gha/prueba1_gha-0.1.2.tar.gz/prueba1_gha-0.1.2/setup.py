# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prueba1_gha']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'prueba1-gha',
    'version': '0.1.2',
    'description': 'Prueba Github actions',
    'long_description': '## Readme\n\n\n\n\n[![PyPI](https://img.shields.io/pypi/v/prueba1-gha?logo=pypi&logoColor=white&style=for-the-badge)](https://pypi.org/project/prueba1-gha/)\n\n',
    'author': 'Martin More',
    'author_email': 'martinmore@mail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://example.com/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
