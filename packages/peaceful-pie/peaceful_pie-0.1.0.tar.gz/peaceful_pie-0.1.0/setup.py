# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['peaceful_pie']

package_data = \
{'': ['*']}

install_requires = \
['chili>=1.8.0,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'peaceful-pie',
    'version': '0.1.0',
    'description': 'Control Unity from Python!',
    'long_description': '# Peaceful Pie\n\nConnect python with unity for reinforcement learning!\n',
    'author': 'Hugh Perkins',
    'author_email': 'hughperkins@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
