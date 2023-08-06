# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rplus_graphdb',
 'rplus_graphdb.connection',
 'rplus_graphdb.interface',
 'rplus_graphdb.schema',
 'rplus_graphdb.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0',
 'gremlinpython>=3.5.2,<4.0.0',
 'pathlib>=1.0.1,<2.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'websockets>=10.3,<11.0']

setup_kwargs = {
    'name': 'rplus-graphdb-module',
    'version': '0.0.3',
    'description': '',
    'long_description': '# Rplus graphdb module\n\n## To install requirements to virtual environment\n\n```shell\n    make pip\n```\n\n## Activate virtualenv\n```shell\n  poetry env use $(which python)\n```\n\n## Install dependencies\n```shell\n  make install\n```\n\n## Update dependencies\n```shell\n  make update\n```\n\n## To build package\n```shell\n  make build\n```\n\n## To publish package\n```shell\n  make publish\n```\n',
    'author': 'AIML Team',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
