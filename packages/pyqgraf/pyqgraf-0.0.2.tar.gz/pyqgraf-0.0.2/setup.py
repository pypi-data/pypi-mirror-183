# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyqgraf']

package_data = \
{'': ['*']}

install_requires = \
['requests', 'scikit-build', 'smpl']

setup_kwargs = {
    'name': 'pyqgraf',
    'version': '0.0.2',
    'description': 'PyQgraf is a Python wrapper for Qgraf, a Feynman diagram generator.',
    'long_description': 'pyqgraf',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/APN-Pucky/pyqgraf',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
