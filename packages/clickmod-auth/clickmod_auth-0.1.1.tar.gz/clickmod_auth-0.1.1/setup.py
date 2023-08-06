# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clickmod_auth']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0', 'python-gnupg>=0.5.0,<0.6.0', 'rich>=12.5.1,<13.0.0']

entry_points = \
{'clickmod': ['auth = clickmod_auth.plugin:plugin']}

setup_kwargs = {
    'name': 'clickmod-auth',
    'version': '0.1.1',
    'description': 'ClickMod authentication module.',
    'long_description': '# ClickMod Auth\n\nTODO\n',
    'author': 'Luke Hodkinson',
    'author_email': 'furious.luke@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
