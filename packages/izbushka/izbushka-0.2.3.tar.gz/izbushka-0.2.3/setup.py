# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['izbushka']

package_data = \
{'': ['*']}

install_requires = \
['PyPika>=0.48.9,<0.49.0',
 'PyYAML<6',
 'click>=8.1.3,<9.0.0',
 'clickhouse-connect>=0.4.1,<0.5.0',
 'natsort>=8.2.0,<9.0.0']

setup_kwargs = {
    'name': 'izbushka',
    'version': '0.2.3',
    'description': '',
    'long_description': None,
    'author': 'Anton Evdokimov',
    'author_email': 'meowmeowcode@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
