# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['diodedance']

package_data = \
{'': ['*']}

install_requires = \
['pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'diodedance',
    'version': '0.1.0',
    'description': 'Library for controlling Diodedance boards over UDP.',
    'long_description': '# diodedance\nControl library for Diodedance IoT boards.\n',
    'author': 'perpetualCreations',
    'author_email': 'tchen0584@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
