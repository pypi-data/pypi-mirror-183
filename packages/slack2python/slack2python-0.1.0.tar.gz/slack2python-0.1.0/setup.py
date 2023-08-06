# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slack2python']

package_data = \
{'': ['*']}

install_requires = \
['slack-bolt>=1.16.1,<2.0.0']

setup_kwargs = {
    'name': 'slack2python',
    'version': '0.1.0',
    'description': 'a python wrapper of slack bolt',
    'long_description': '# slack2python\na python wrapper of slack bolt\n',
    'author': '2lu3',
    'author_email': 'hi2lu3@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
