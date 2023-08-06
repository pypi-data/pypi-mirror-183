# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rplus_offline_result']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rplus-offline-result-module',
    'version': '0.0.3',
    'description': '',
    'long_description': '# Rplus offline-result-module\n\n## To install requirements to virtual environment\n\n```shell\n    make pip\n```\n\n## Activate virtualenv\n```shell\n  poetry env use $(which python)\n```\n\n## Install dependencies\n```shell\n  make install\n```\n\n## Update dependencies\n```shell\n  make update\n```\n\n## To build package\n```shell\n  make build\n```\n\n## To publish package\n```shell\n  make publish\n```\n',
    'author': 'AIML Team',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
