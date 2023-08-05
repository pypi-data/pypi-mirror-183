# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dnsctl']

package_data = \
{'': ['*'], 'dnsctl': ['templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'click>=8.1.3,<9.0.0',
 'dynaconf>=3.1.11,<4.0.0',
 'loguru>=0.6.0,<0.7.0',
 'pathlib2>=2.3.7,<3.0.0',
 'rich-click>=1.4,<2.0']

entry_points = \
{'console_scripts': ['dnsctl = dnsctl.__main__:cli']}

setup_kwargs = {
    'name': 'dnsctl',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Gabriel',
    'author_email': 'gabrielmello808@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
