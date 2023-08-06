# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['statespace', 'statespace.models', 'statespace.processors']

package_data = \
{'': ['*']}

install_requires = \
['filterpy', 'matplotlib', 'numpy', 'scipy']

setup_kwargs = {
    'name': 'statespace',
    'version': '1.6.2',
    'description': '',
    'long_description': 'None',
    'author': 'noah smith',
    'author_email': 'noah@statespace.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
