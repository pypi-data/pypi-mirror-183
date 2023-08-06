# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sideshiftpy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sideshiftpy',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'niglet',
    'author_email': '-@x.x',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
