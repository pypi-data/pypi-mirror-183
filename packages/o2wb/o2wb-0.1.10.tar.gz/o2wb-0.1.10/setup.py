# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['o2wb']

package_data = \
{'': ['*']}

install_requires = \
['argparse>=1.4.0,<1.5.0',
 'html5lib>=1.1.0,<1.2.0',
 'rdflib>=6.2.0,<6.3.0',
 'wikibaseintegrator>=0.12.2,<0.13.0']

entry_points = \
{'console_scripts': ['o2wb-exp = o2wb.exp:main', 'o2wb-imp = o2wb.imp:main']}

setup_kwargs = {
    'name': 'o2wb',
    'version': '0.1.10',
    'description': '',
    'long_description': '',
    'author': 'DPKM',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
