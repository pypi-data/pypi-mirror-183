# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aiodo']

package_data = \
{'': ['*']}

install_requires = \
['python-configuration>=0.8.2,<0.9.0', 'zeroconf>=0.47.1,<0.48.0']

entry_points = \
{'aiodo.device': ['Dummy = aiodo.dummy:get_device'],
 'console_scripts': ['aiodo = aiodo.core:main']}

setup_kwargs = {
    'name': 'aiodo',
    'version': '0.1.0',
    'description': 'asynchronous ditributed objects',
    'long_description': '# aiodo\n\nAsynchronous first distributed objects',
    'author': 'Jose Tiago Macara Coutinho',
    'author_email': 'coutinhotiago@gmail.com',
    'maintainer': 'Jose Tiago Macara Coutinho',
    'maintainer_email': 'coutinhotiago@gmail.com',
    'url': 'https://github.com/tiagocoutinho/aiodo',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
