# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coconut_cli']

package_data = \
{'': ['*']}

install_requires = \
['inquirer>=3.1.1,<4.0.0', 'pyfiglet>=0.8.post1,<0.9']

setup_kwargs = {
    'name': 'coconut-cli',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Arpan Pandey',
    'author_email': 'arpan@hackersreboot.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
