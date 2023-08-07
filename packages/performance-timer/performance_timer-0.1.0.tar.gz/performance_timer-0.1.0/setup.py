# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['performance_timer']

package_data = \
{'': ['*']}

install_requires = \
['shortuuid>=1.0.11,<2.0.0']

setup_kwargs = {
    'name': 'performance-timer',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Project performance_timer\n\n... project desc ...\n\n----\n\n... more ...',
    'author': 'Thibaut Stalin',
    'author_email': 'thibaut.st@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
