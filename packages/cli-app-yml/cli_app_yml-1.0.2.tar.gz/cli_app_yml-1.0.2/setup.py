# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cli']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.21.0,<0.22.0', 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['cli = cli:run']}

setup_kwargs = {
    'name': 'cli-app-yml',
    'version': '1.0.2',
    'description': 'CLI application creater based out of argparse. entrypoints for different subcommands are defined using yml',
    'long_description': '',
    'author': 'Varun Bhat',
    'author_email': 'varunbhat@apple.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
