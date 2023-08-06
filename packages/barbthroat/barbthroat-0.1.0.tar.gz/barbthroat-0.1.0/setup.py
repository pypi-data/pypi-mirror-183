# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['barbthroat',
 'barbthroat.connectors',
 'barbthroat.custodians',
 'barbthroat.indicators',
 'barbthroat.storages']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0',
 'aiolimiter>=1.0.0,<2.0.0',
 'asyncstdlib>=3.10.5,<4.0.0',
 'simplejson>=3.18.0,<4.0.0',
 'tenacity>=8.1.0,<9.0.0']

setup_kwargs = {
    'name': 'barbthroat',
    'version': '0.1.0',
    'description': 'A library to help write directional strategies for Hummingbot.',
    'long_description': '# barbthroat\nA library to help write directional strategies for Hummingbot.\n',
    'author': 'discosultan',
    'author_email': 'jaanusvarus@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
