# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['monazco', 'monazco.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'monazco',
    'version': '0.1.1',
    'description': 'gym-like enviornment for the game Monazco, as well as the option to run in the terminal',
    'long_description': 'monazco game\n\nUse run.py to play in the console\nuse monazco.monazcoEnv() to run the game as a gym-like environment\n\nPlease see board.jpg for a picture of what the board looks like, so you can understand the tests and stuff',
    'author': 'Charlie',
    'author_email': 'CharlieJackGaynor@Gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
