# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['event_logger']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'event-logger',
    'version': '999999.0.0',
    'description': 'Event Logger',
    'long_description': 'Event Logger\n==============================\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/event-logger?style=plastic)\n![PyPI](https://img.shields.io/pypi/v/event-logger?color=informational&style=plastic)\n\nUpload dummy package to PyPI in order to demonstrate dependency confusion attack.\n\n',
    'author': 'Mercari',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)
