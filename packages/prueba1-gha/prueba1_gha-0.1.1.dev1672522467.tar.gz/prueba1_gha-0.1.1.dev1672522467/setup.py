# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prueba1_gha']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'prueba1-gha',
    'version': '0.1.1.dev1672522467',
    'description': 'Prueba Github actions',
    'long_description': '## Readme\n\nreadme\n',
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
