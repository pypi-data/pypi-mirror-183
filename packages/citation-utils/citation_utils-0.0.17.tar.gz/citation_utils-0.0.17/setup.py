# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['citation_utils']

package_data = \
{'': ['*'], 'citation_utils': ['sql/legacy/*']}

install_requires = \
['citation-docket>=0.0.12,<0.0.13',
 'citation-report>=0.0.9,<0.0.10',
 'loguru>=0.6.0,<0.7.0',
 'pydantic>=1.10.3,<2.0.0',
 'python-slugify>=6.1.2,<7.0.0',
 'sqlite-utils>=3.30,<4.0']

setup_kwargs = {
    'name': 'citation-utils',
    'version': '0.0.17',
    'description': 'Regex-pattern matching docket / report citations in Philippine Supreme Court Decisions.',
    'long_description': 'None',
    'author': 'Marcelino G. Veloso III',
    'author_email': 'mars@veloso.one',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.11.0',
}


setup(**setup_kwargs)
