# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onf_rtm']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.2,<4.0.0',
 'numpy>=1.24.1,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pyshp>=2.3.1,<3.0.0',
 'rdp>=0.8,<0.9',
 'scipy>=1.9.3,<2.0.0',
 'simpledbf>=0.2.6,<0.3.0',
 'visvalingamwyatt>=0.2.0,<0.3.0']

setup_kwargs = {
    'name': 'onf-rtm',
    'version': '1.0.1',
    'description': '',
    'long_description': 'None',
    'author': 'ONF-RTM',
    'author_email': 'clement.roussel@onf.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
