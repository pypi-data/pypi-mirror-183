# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['encosy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'encosy',
    'version': '0.9.8',
    'description': 'ECS python implementation',
    'long_description': '# encosy\n',
    'author': 'baranynah',
    'author_email': 'a.kovalenko.ai@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
