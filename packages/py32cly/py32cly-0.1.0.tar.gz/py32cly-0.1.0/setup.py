# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py32cly']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py32cly',
    'version': '0.1.0',
    'description': 'A basic dm clear.;',
    'long_description': '',
    'author': 'Tark',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
