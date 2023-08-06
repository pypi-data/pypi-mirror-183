# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['going']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'going',
    'version': '0.1.0',
    'description': 'Event-driven support',
    'long_description': 'Going\n=====\n\nEvent-driven support\n',
    'author': 'Konrad Rymczak',
    'author_email': 'me@teserak.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
