# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cli', 'cli.commands', 'cli.upsolver']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.3,<9.0.0',
 'requests>=2.27.1,<3.0.0',
 'tabulate>=0.8.9,<0.9.0',
 'yarl>=1.7.2,<2.0.0']

entry_points = \
{'console_scripts': ['upsolver = cli.main:main']}

setup_kwargs = {
    'name': 'upsolver-cli',
    'version': '0.6.1',
    'description': "Upsolver's CLI",
    'long_description': 'None',
    'author': 'alexyavo',
    'author_email': 'alex@upsolver.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/upsolver/cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
