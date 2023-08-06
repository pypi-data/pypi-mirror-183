# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['n6ai']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'n6ai',
    'version': '0.0.0',
    'description': 'Placeholder for PyPi package.',
    'long_description': 'None',
    'author': 'Sergej Samsonenko',
    'author_email': 'contact@sergej.codes',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
