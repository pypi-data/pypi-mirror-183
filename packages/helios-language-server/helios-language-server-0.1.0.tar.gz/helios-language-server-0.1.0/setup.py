# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['helios_ls']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'pygls>=0.13.1,<0.14.0', 'tree-sitter>=0.20.1,<0.21.0']

entry_points = \
{'console_scripts': ['helios-language-server = helios_ls.server:main']}

setup_kwargs = {
    'name': 'helios-language-server',
    'version': '0.1.0',
    'description': 'Language server for Helios, a non-Haskell Cardano smart contract DSL.',
    'long_description': 'None',
    'author': 'et',
    'author_email': 'et',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10.0,<3.11.0',
}


setup(**setup_kwargs)
