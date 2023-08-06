# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['textarium', 'textarium.tests']

package_data = \
{'': ['*'], 'textarium': ['collections/*']}

install_requires = \
['nltk>=3.8.1,<4.0.0', 'pytest>=7.1.3,<8.0.0', 'setuptools>=65.6.3,<66.0.0']

setup_kwargs = {
    'name': 'textarium',
    'version': '0.1.0',
    'description': 'Package for text cleaning and processing',
    'long_description': '# textarium\nTextarium is a Python package for text processing.\n',
    'author': '6b656b',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
