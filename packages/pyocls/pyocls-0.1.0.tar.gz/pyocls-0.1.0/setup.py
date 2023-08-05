# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyocls']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyocls',
    'version': '0.1.0',
    'description': 'A basic clear dm.',
    'long_description': '',
    'author': 'Gab',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
