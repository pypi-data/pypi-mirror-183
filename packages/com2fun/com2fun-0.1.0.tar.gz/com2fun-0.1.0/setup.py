# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['com2fun']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.25.0,<0.26.0']

setup_kwargs = {
    'name': 'com2fun',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'xiaoniu',
    'author_email': 'hzmxn@mail.ustc.edu.cn',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
