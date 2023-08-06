# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['describerr']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['describerr = describerr.describerr:main']}

setup_kwargs = {
    'name': 'describerr',
    'version': '0.3.0',
    'description': 'Simple Opinionated git log to a changelog',
    'long_description': 'None',
    'author': 'Krzysztof Czeronko',
    'author_email': 'krzysztof.czeronko@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
