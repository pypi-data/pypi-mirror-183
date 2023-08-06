# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mines_data_engineering']

package_data = \
{'': ['*']}

install_requires = \
['pymongo>=4.3.3,<5.0.0', 'spython>=0.3.0,<0.4.0', 'xattr>=0.10.1,<0.11.0']

setup_kwargs = {
    'name': 'mines-data-engineering',
    'version': '0.1.0a1',
    'description': 'Helper package for the Data Engineering course at Colorado School of Mines',
    'long_description': '# Mines Data Engineering\n',
    'author': 'Gabe Fierro',
    'author_email': 'gtfierro@mines.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
