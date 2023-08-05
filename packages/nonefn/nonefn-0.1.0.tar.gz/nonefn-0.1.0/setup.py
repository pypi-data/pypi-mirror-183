# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonefn']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'nonefn',
    'version': '0.1.0',
    'description': "Some usefull functions you don't want to write again",
    'long_description': '',
    'author': 'hglong16',
    'author_email': 'intihad.vuong@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hglong16/nonefn',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
