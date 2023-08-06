# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['citation_report']

package_data = \
{'': ['*']}

install_requires = \
['citation-date>=0.0.5,<0.0.6']

setup_kwargs = {
    'name': 'citation-report',
    'version': '0.0.9',
    'description': 'Parse legal citations having the publisher format - i.e. SCRA, PHIL, OFFG - referring to Philippine Supreme Court decisions.',
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
