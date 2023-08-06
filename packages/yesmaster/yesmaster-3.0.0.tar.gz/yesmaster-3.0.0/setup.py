# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yesmaster', 'yesmaster.algo']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['yesmaster = yesmaster.yesmaster:run']}

setup_kwargs = {
    'name': 'yesmaster',
    'version': '3.0.0',
    'description': "Yesmaster is a terminal mastermind game. It's possible to play normally or let's play the computer with algorithm.",
    'long_description': 'None',
    'author': 'matteli',
    'author_email': 'matthieu.nue@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/matteli/yesmaster',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
