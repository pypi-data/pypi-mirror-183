# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['utils_module',
 'utils_module.custom_exception',
 'utils_module.jwt',
 'utils_module.logger',
 'utils_module.s3_service',
 'utils_module.utils']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.20.50,<2.0.0',
 'pandas>=1.4.0,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyjwt>=2.4.0,<3.0.0',
 'rplus-constants-module>=0.0.4,<0.0.5']

setup_kwargs = {
    'name': 'rplus-utils-module',
    'version': '0.0.2',
    'description': '',
    'long_description': '# rplus utils module\n\n## To install requirements to virtual environment\n\n```shell\n    make pip\n```\n\n## Activate virtualenv\n\n```shell\n  poetry env use $(which python)\n```\n\n## Install dependencies\n\n```shell\n  make install\n```\n\n## Update dependencies\n\n```shell\n  make update\n```\n\n## To build package\n\n```shell\n  make build\n```\n\n## To publish package\n\n```shell\n  make publish\n```\n',
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
