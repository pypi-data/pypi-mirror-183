# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stop_the_vcr']

package_data = \
{'': ['*']}

install_requires = \
['vcrpy>=4.2.1,<5.0.0']

setup_kwargs = {
    'name': 'stop-the-vcr',
    'version': '0.1.2',
    'description': 'A package that contains VCR.py custom request matchers',
    'long_description': 'None',
    'author': 'Alex Cornelio',
    'author_email': 'ascornelio@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
