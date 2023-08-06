# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sbux', 'sbux.models']

package_data = \
{'': ['*']}

install_requires = \
['dataclasses-json>=0.5.7,<0.6.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'sbux',
    'version': '0.2.1',
    'description': 'An unofficial Starbucks Singapore (SG) software development kit (SDK).',
    'long_description': '# sbux\n\n`sbux` is an unofficial Starbucks Singapore (SG) software development kit (SDK). SBUX is the ticker symbol of Starbucks Corporation on the NASDAQ.\n\n## Installing\n\nInstall and update using `pip`;\n\n```sh\npip install sbux\n```\n\n## A Simple Example\n\n```python\nfrom sbux import Starbucks\n\napp = Starbucks\napp.get_stores()\napp.get_menu_items(branch_code="13377")\n```\n\n## Contributing\n\nFor guidance on setting up a development environment and how to make a contribution, see the [contributing guidelines](./docs/CONTRIBUTING.md).\n',
    'author': 'Jerry Ng',
    'author_email': 'ngshiheng@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ngshiheng/sbux',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
