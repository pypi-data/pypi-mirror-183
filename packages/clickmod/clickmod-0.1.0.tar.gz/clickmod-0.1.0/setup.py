# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clickmod']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0', 'requests>=2.28.1,<3.0.0', 'rich>=12.5.1,<13.0.0']

setup_kwargs = {
    'name': 'clickmod',
    'version': '0.1.0',
    'description': 'Click CLI modules.',
    'long_description': '# ClickMod\n\nTODO\n\n',
    'author': 'Luke Hodkinson',
    'author_email': 'furious.luke@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
