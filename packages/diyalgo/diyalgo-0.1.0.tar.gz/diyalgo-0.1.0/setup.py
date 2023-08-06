# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['diyalgo',
 'diyalgo.client',
 'diyalgo.expansions',
 'diyalgo.features',
 'diyalgo.models']

package_data = \
{'': ['*']}

install_requires = \
['Mastodon.py>=1.8.0,<2.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'lxml>=4.9.2,<5.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'sqlmodel>=0.0.8,<0.0.9']

setup_kwargs = {
    'name': 'diyalgo',
    'version': '0.1.0',
    'description': 'DIY Algorithms for Mastodon',
    'long_description': '# diyalgo\n\nDIY Algoritms for mastodon\n\nJust uploading to PyPI for now to squat on the package name. Will release\nah um a version of this soon :)',
    'author': 'sneakers-the-rat',
    'author_email': 'JLSaunders987@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
