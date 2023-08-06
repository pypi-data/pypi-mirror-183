# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smpl_util']

package_data = \
{'': ['*']}

install_requires = \
['numpy', 'smpl_doc']

setup_kwargs = {
    'name': 'smpl-util',
    'version': '1.0.6',
    'description': 'SiMPLe plotting and fitting',
    'long_description': 'smpl_io\n',
    'author': 'Alexander Puck Neuwirth',
    'author_email': 'alexander@neuwirth-informatik.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/APN-Pucky/smpl_util',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
