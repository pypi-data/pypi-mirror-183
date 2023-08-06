# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xontrib', 'xontrib.zoxide']

package_data = \
{'': ['*']}

install_requires = \
['xonsh>=0.12.5']

setup_kwargs = {
    'name': 'xontrib-zoxide',
    'version': '1.0.0',
    'description': 'Zoxide integration for xonsh',
    'long_description': '<p align="center">\nZoxide integration for xonsh\n</p>\n\n<p align="center">  \nIf you like the idea click ⭐ on the repo and stay tuned.\n</p>\n\n\n## Requirements\n\nYou need [zoxide](https://github.com/ajeetdsouza/zoxide) installed on your system. See [install instructions](https://github.com/ajeetdsouza/zoxide#step-1-installing-zoxide) to get it.\n\n## Installation\n\nTo install use pip:\n\n```bash\nxpip install xontrib-zoxide\n# or: xpip install -U git+https://github.com/dyuri/xontrib-zoxide\n```\n\n## Usage\n\n```bash\nxontrib load zoxide\nz folder\n```\n\nSee [zoxide](https://github.com/ajeetdsouza/zoxide) for detailed usage.\n\n## Credits\n\nThis package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).\n\n',
    'author': 'Gyuri Horak',
    'author_email': 'dyuri@horak.hu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dyuri/xontrib-zoxide',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
