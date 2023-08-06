# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['citation_docket', 'citation_docket.base', 'citation_docket.regexes']

package_data = \
{'': ['*']}

install_requires = \
['citation-date>=0.0.5,<0.0.6', 'pydantic>=1.10.3,<2.0.0']

setup_kwargs = {
    'name': 'citation-docket',
    'version': '0.0.12',
    'description': 'Parse legal citations having the docket format - i.e. GR, AM, AC, BM - referring to Philippine Supreme Court decisions.',
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
