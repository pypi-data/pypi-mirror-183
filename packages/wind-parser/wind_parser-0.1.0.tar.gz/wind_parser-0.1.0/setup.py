# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wind_parser']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'wind-parser',
    'version': '0.1.0',
    'description': 'Python Wind Parser is a parser used to retrieve and manipulate arguments for command line interfaces',
    'long_description': '# wind-parser\nPython wind parser is a parser used to retrieve and manipulate arguments for command line interfaces\n',
    'author': 'Anthony Rafidison',
    'author_email': 'benjaraf006@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
