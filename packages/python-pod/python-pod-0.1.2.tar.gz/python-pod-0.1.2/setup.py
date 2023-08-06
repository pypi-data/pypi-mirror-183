# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypod']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'pyaudio>=0.2.12,<0.3.0',
 'rich>=13.0.0,<14.0.0',
 'textual>=0.9.1,<0.10.0']

entry_points = \
{'console_scripts': ['pypod = pypod.cli:cli']}

setup_kwargs = {
    'name': 'python-pod',
    'version': '0.1.2',
    'description': 'Python terminal music player',
    'long_description': '## PyPod\n\n[![PyPI](https://img.shields.io/pypi/v/python-pod)](https://pypi.org/project/python-pod/)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-pod)\n\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![EditorConfig](https://img.shields.io/badge/-EditorConfig-grey?logo=editorconfig)](https://editorconfig.org/)\n[![semantic-release: angular](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)\n\n\n![screenshot](https://github.com/bmwant/pypod/blob/main/assets/player_ui.png)\n\n\nPython console music player\n\n### Installation\n\n```bash\n$ pip install python-pod\n```\n\n### Usage\n```bash\n$ pypod <path-to-directory>  # play everything under the folder\n$ pypod filename.wav  # play single file\n```\n\n### Development\n\n```bash\n$ brew install portaudio\n$ poetry install --with dev\n\n$ make debug  # run app in debug mode\n$ make console  # run textual dev console\n```\n',
    'author': 'Misha Behersky',
    'author_email': 'bmwant@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
