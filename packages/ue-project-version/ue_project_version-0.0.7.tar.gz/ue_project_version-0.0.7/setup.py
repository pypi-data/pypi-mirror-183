# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bootloader',
 'bootloader.unreal_engine',
 'bootloader.unreal_engine.cli',
 'bootloader.unreal_engine.utils']

package_data = \
{'': ['*']}

install_requires = \
['perseus-core-library>=1.18.0,<2.0.0']

entry_points = \
{'console_scripts': ['ueprjver = bootloader.unreal_engine.cli.ueprjver:run']}

setup_kwargs = {
    'name': 'ue-project-version',
    'version': '0.0.7',
    'description': 'Unreal Engine project version utility',
    'long_description': '# Unreal Project Version Utility\nCommand-line interface utility for manipulating the project version of an Unreal Engine project.\n\n```shell\nueprjver --path .  --build-number 237\n```\n',
    'author': 'Daniel CAUNE',
    'author_email': 'daniel.caune@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Bootloader-Studio/ue-project-version',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
