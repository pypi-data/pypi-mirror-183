# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qctrlcommons',
 'qctrlcommons.graphql',
 'qctrlcommons.node',
 'qctrlcommons.validation']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0',
 'graphql-core>=3.2.1,<3.3.0',
 'inflection>=0.5.1,<0.6.0',
 'jsonschema>=4.14,<5.0',
 'numpy>=1.21.5,<2.0.0',
 'python-forge>=18.6.0,<19.0.0',
 'scipy>=1.7.3',
 'toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'qctrl-commons',
    'version': '17.7.0',
    'description': 'Q-CTRL Commons',
    'long_description': '# Q-CTRL Commons\n\nQ-CTRL Commons is a collection of common libraries for the Python language.\n',
    'author': 'Q-CTRL',
    'author_email': 'support@q-ctrl.com',
    'maintainer': 'Q-CTRL',
    'maintainer_email': 'support@q-ctrl.com',
    'url': 'https://q-ctrl.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.2,<3.11',
}


setup(**setup_kwargs)
