# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cloudops', 'cloudops.secret_manager', 'cloudops.secret_manager.aws']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.37,<2.0.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'cloudops-secret-manager-aws',
    'version': '0.1.0',
    'description': 'The cloudops-secret-manager-aws package',
    'long_description': '# cloudops-secret-manager-aws\n',
    'author': 'Manuel Castillo',
    'author_email': 'manucalop@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/manucalop/cloudops-secret-manager-aws',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
