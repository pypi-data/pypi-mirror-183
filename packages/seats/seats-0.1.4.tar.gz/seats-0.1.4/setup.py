# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seats',
 'seats.cli',
 'seats.cli.cmdbs',
 'seats.cli.connectors',
 'seats.cli.notebooks',
 'seats.clients',
 'seats.cmdbs',
 'seats.connectors',
 'seats.connectors.fortigate',
 'seats.models']

package_data = \
{'': ['*'], 'seats': ['notebooks/*']}

install_requires = \
['pyyaml>=6.0,<7.0', 'requests>=2.28.1,<3.0.0', 'xmltodict>=0.13.0,<0.14.0']

extras_require = \
{'all': ['click>=8.1.3,<9.0.0', 'jupyter>=1.0.0,<2.0.0', 'flask>=2.2.2,<3.0.0'],
 'cli': ['click>=8.1.3,<9.0.0'],
 'flaskapp': ['flask>=2.2.2,<3.0.0'],
 'notebooks': ['jupyter>=1.0.0,<2.0.0']}

entry_points = \
{'console_scripts': ['seats = seats.cli.cli:entry_point']}

setup_kwargs = {
    'name': 'seats',
    'version': '0.1.4',
    'description': 'Security Engineering Automation Tool Set',
    'long_description': '# seats\nSecurity Engineering Automation Toll Set\n',
    'author': 'Thiago Takayama',
    'author_email': 'thiago@takayama.co.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
