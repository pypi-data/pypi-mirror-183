# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['derivation']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'derivation',
    'version': '0.1.0',
    'description': '',
    'long_description': '# variants',
    'author': 'Rain Wu',
    'author_email': 'rain.wu@appier.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
