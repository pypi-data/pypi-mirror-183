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
    'version': '0.2.0',
    'description': 'Control Unity from Python!',
    'long_description': '# Peaceful Pie\n\nConnect Python with Unity for reinforcement learning!\n\n## Installation\n\nYou need to install both into Unity project, and into your Python environment.\n\n### In Unity\n\n- in Unity, in your project\'s "Assets" folder, create a "Plugins" folder, if it doesn\'t already exist\n- First install AustinHarris.JsonRPC:\n    - Download https://www.nuget.org/api/v2/package/AustinHarris.JsonRpc/1.2.3\n    - rename to have filename suffix be `.zip` (you might need to turn on options to see all file extensions)\n    - unzip the resulting zip file\n    - copy `lib/netstandard2.1/AustinHarris.JsonRpc.dll` into your `Plugins` folder\n    - select the file, in your Plugins, and in \'Inspector\' unselect \'validate references\', and click \'Apply\'\n- from this repo, copy `PeacefulPie.dll` into your `Plugins` folder\n    - select the file, in your Plugins, and in \'Inspector\' unselect \'validate references\', and click \'Apply\'\n- if on Mac silicon, make sure to change \'CPU\' to \'Any CPU\', for each dll, clicking \'Apply\' each time\n\nYou should be good to go :)\n\n### In Python\n\n```\npip install -U peaceful-pie\n```\n',
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
