# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src\\main\\python'}

packages = \
['evofond']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.2,<4.0.0',
 'numpy>=1.24.1,<2.0.0',
 'pandas>=1.5.2,<2.0.0',
 'scipy>=1.9.3,<2.0.0']

setup_kwargs = {
    'name': 'evofond',
    'version': '0.0.0',
    'description': '',
    'long_description': 'None',
    'author': 'ONF-RTM',
    'author_email': 'None',
    'maintainer': 'Clément Roussel',
    'maintainer_email': 'clement.roussel@onf.fr',
    'url': 'https://www.onf.fr/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
