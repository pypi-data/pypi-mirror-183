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
    'version': '3.0.1',
    'description': "Yesmaster is a terminal mastermind game. It's possible to play normally or let's play the computer with algorithm.",
    'long_description': "Yes Master\n==========\nGoal\n----\nYesmaster is a terminal mastermind game. It's possible to play normally or let's play the computer with algorithm :\n- random_idiot : totally random and idiot\n- random_no_repeat : random but never the same code twice\n- compatible : play random but take in consideration the verification and play only code compatible with it\n- compatible_8in2 : play the two first code with 8 colors and after that play compatible\n- compatible_4in1 : play like compatible but the first must be 4 differents colors\n- one_step_ahead : play the move that has the highest expected elimination\n\nInstallation\n------------\nThe program is available on [Pypi](https://pypi.org/project/yesmaster/).\nYou need at least python 3.6 and you can use pipx to install it.\n```\npipx install yesmaster\n```\n\nUsage\n-----\n```\nusage: yesmaster.py [-h] [--algo ALGO] [--loop LOOP] {play,auto}\n\npositional arguments:{play,auto}  play yourself or let's computer playing\n\noptional arguments:\n  -h, --help   show this help message and exit\n  --algo ALGO  Choose an algo present in the algo folder\n  --loop LOOP  Number of games\n```\nTest your algorithm\n-------------------\nYou can add your personnal algorithm with a python file in the algo directory (the name of the python file will be the name of the algo to call in the command line). A template file shows you how your algo must be organized. Two functions are mandatory in a class name Algo :\n- get(self) : executed for choosing the code. Must return a 4 letters string with letters among ROGBYAPW\n- report(self, test, good, bad) : executed with 3 arguments (test : the code that you pushed with get, good : the number of goods colors at good place, bad : the number of goods colors at wrong place). Return nothing.\n\n",
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
