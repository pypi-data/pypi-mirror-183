# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['teamgenerator']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'teamgenerator',
    'version': '1.0',
    'description': 'Use the createteam function to input two peramers list of strings (participants) and a integer (amtofteams) . It will then display the teams',
    'long_description': None,
    'author': 'Aidan',
    'author_email': 'aidan.faulding@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
