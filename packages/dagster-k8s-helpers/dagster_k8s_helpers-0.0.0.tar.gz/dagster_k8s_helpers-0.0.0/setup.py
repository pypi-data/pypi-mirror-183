# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dagster_k8s_helpers']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dagster-k8s-helpers',
    'version': '0.0.0',
    'description': '',
    'long_description': '',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.github.com/alrudolph/dagster_k8s_helpers',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
