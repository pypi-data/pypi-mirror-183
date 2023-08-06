# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['citation_date', 'citation_date.base']

package_data = \
{'': ['*']}

install_requires = \
['python-dateutil>=2.8,<3.0', 'types-python-dateutil>=2.8.19,<3.0.0']

setup_kwargs = {
    'name': 'citation-date',
    'version': '0.0.5',
    'description': 'Regex date formula and decoder - Philippine Supreme Court Decisions',
    'long_description': 'None',
    'author': 'Marcelino G. Veloso III',
    'author_email': 'mars@veloso.one',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
