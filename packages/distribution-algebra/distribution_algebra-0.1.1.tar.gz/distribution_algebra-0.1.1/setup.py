# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['distribution_algebra', 'distribution_algebra.examples', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0',
 'matplotlib>=3.6.2,<4.0.0',
 'numpy>=1.24.0,<2.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'scipy>=1.9.3,<2.0.0',
 'wheel>=0.38.1']

setup_kwargs = {
    'name': 'distribution-algebra',
    'version': '0.1.1',
    'description': ' A python package that implements an easy-to-use interface to random variables, statistical distributions, and their algebra.',
    'long_description': 'None',
    'author': 'Vaibhav Karve',
    'author_email': 'vkarve@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
