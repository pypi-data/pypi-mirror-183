# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quiltplus']

package_data = \
{'': ['*'], 'quiltplus': ['config/*']}

install_requires = \
['fondat>=4.0.19,<5.0.0', 'quilt3>=5.1.0,<6.0.0']

setup_kwargs = {
    'name': 'quiltplus',
    'version': '0.1.0',
    'description': "Resource-oriented Python API for Quilt's decentralized social knowledge platform",
    'long_description': "# quiltplus\nResource-oriented API for Quilt's decentralized social knowledge platform\n\n# Developmment\n## Setup\n\n```\ngit clone https://github.com/quiltdata/quiltplus\ncd quiltplus\npoetry self update\npoetry install\npoetry run pytest-watch\n```\n## Pushing Changes\n```\npoetry version\npoetry publish\n```",
    'author': 'Ernest Prabhakar',
    'author_email': 'ernest@quiltdata.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
