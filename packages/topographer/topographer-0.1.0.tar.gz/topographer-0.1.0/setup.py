# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['topographer']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'topographer',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Zach Probst',
    'author_email': 'zprobst@resilientvitality.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
