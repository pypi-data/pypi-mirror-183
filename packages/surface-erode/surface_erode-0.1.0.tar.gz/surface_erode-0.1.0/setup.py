# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['surface_erode']

package_data = \
{'': ['*'], 'surface_erode': ['src/*']}

install_requires = \
['importlib-metadata>=5.0.0,<6.0.0', 'numpy>=1.20.0,<2.0.0']

setup_kwargs = {
    'name': 'surface-erode',
    'version': '0.1.0',
    'description': 'erode medical image surface',
    'long_description': '',
    'author': '安兴乐',
    'author_email': 'anxingle@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
