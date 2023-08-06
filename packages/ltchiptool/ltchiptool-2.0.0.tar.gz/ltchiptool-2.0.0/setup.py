# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ltchiptool',
 'ltchiptool.commands',
 'ltchiptool.commands.flash',
 'ltchiptool.models',
 'ltchiptool.soc',
 'ltchiptool.soc.ambz',
 'ltchiptool.soc.ambz.util',
 'ltchiptool.soc.ambz2',
 'ltchiptool.soc.ambz2.util',
 'ltchiptool.soc.bk72xx',
 'ltchiptool.soc.bk72xx.util',
 'ltchiptool.util',
 'uf2tool',
 'uf2tool.binpatch',
 'uf2tool.models',
 'uf2tool.upload']

package_data = \
{'': ['*']}

install_requires = \
['bk7231tools>=1.2.1,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'colorama>=0.4.5,<0.5.0',
 'importlib-metadata>=4.12.0,<5.0.0',
 'prettytable>=3.3.0,<4.0.0',
 'pycryptodomex>=3.15.0,<4.0.0',
 'xmodem>=0.4.6,<0.5.0']

entry_points = \
{'console_scripts': ['ltchiptool = ltchiptool:cli']}

setup_kwargs = {
    'name': 'ltchiptool',
    'version': '2.0.0',
    'description': 'Tools for working with LT-supported IoT chips',
    'long_description': 'None',
    'author': 'Kuba Szczodrzyński',
    'author_email': 'kuba@szczodrzynski.pl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
