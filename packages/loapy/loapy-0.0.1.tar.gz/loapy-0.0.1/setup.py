# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['loapy']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'loapy',
    'version': '0.0.1',
    'description': 'An asynchronous sdk for lostark offical api.',
    'long_description': '# loapy\n An asynchronous sdk for lostark offical api.\n',
    'author': 'penggin',
    'author_email': '77449586+penggin@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
