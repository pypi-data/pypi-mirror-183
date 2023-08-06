# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cosmonote']

package_data = \
{'': ['*']}

install_requires = \
['clickmod-auth>=0.1.0,<0.2.0',
 'clickmod>=0.1.0,<0.2.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'pytz>=2022.6,<2023.0',
 'timeago>=1.0.16,<2.0.0']

entry_points = \
{'console_scripts': ['cosmo = cosmonote.entrypoint:entrypoint']}

setup_kwargs = {
    'name': 'cosmonote',
    'version': '0.1.4',
    'description': 'Python client to CosmoNote.',
    'long_description': '# CosmoNote\n',
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
