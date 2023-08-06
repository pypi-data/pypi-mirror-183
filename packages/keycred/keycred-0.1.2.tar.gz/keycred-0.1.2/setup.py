# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['keycred']

package_data = \
{'': ['*']}

install_requires = \
['pycryptaes>=0.1.4,<0.2.0', 'pykeepass>=4.0.3,<5.0.0']

setup_kwargs = {
    'name': 'keycred',
    'version': '0.1.2',
    'description': 'Thin wrapper for PyKeePass - a class Credentials to handle it.',
    'long_description': None,
    'author': 'Gwang-Jin Kim',
    'author_email': 'gwang.jin.kim.phd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
