# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lgh']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['lgh = lgh.lgh:main']}

setup_kwargs = {
    'name': 'lazy-ghost-hunters',
    'version': '2.0.2',
    'description': 'Lazy Ghost Hunters is a solver for the game Ghost Hunters from Smart Games',
    'long_description': 'Lazy Ghost Hunters\n==================\n\nGhost Hunters is a little game edited by Smart Games.\nThe goal of the game is to light six ghosts arranged on a 4x4 grid with 6 transparent covers of different sizes on which are drawn 0, 1 or 2 torches.\n\nThe goal of this program is to determine the solution. When the program is launched, indicate 4 rows of 4 numbers 0 (no ghost) or 1 (ghost) to indicate the arrangement of the ghosts. The solution will appear with "o" for the ghosts and colored arrows for the torches.\n',
    'author': 'matteli',
    'author_email': 'matthieu.nue@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/matteli/lazy-ghost-hunters',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
