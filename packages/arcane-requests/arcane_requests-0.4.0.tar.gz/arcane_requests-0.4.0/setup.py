# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arcane']

package_data = \
{'': ['*']}

install_requires = \
['arcane-firebase>=0.2.0,<0.3.0',
 'backoff>=1.10.0,<2.0.0',
 'google-auth>=2.11,<3.0',
 'requests>=2.23.0,<3.0.0',
 'typing-extensions>=3.7']

setup_kwargs = {
    'name': 'arcane-requests',
    'version': '0.4.0',
    'description': 'Utility functions for requests',
    'long_description': '# Arcane requests\n\nThis package helps us to request our different services',
    'author': 'Arcane',
    'author_email': 'product@arcane.run',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
