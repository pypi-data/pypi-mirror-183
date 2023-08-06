# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sigma', 'sigma.backends.stix', 'sigma.pipelines.stix']

package_data = \
{'': ['*']}

install_requires = \
['pysigma>=0.8.10,<0.9.0']

setup_kwargs = {
    'name': 'pysigma-backend-stix',
    'version': '0.1.5',
    'description': 'STIX language backend for pySigma convertor',
    'long_description': 'None',
    'author': 'Cyber-center of Excellence',
    'author_email': 'barha@il.ibm.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/barvhaim/pySigma-backend-stix',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
