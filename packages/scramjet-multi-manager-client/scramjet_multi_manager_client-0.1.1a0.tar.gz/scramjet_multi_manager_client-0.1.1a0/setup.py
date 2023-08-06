# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['multi_manager_client']

package_data = \
{'': ['*']}

install_requires = \
['scramjet-manager-client>=0.1.1a4,<0.2.0']

setup_kwargs = {
    'name': 'scramjet-multi-manager-client',
    'version': '0.1.1a0',
    'description': '',
    'long_description': '<h1 align="center"><strong>Scramjet Multi Manager client</strong></h1>\n\n<p align="center">\n    <a href="https://github.com/scramjetorg/transform-hub/blob/HEAD/LICENSE"><img src="https://img.shields.io/github/license/scramjetorg/transform-hub?color=green&style=plastic" alt="GitHub license" /></a>\n    <a href="https://scr.je/join-community-mg1"><img alt="Discord" src="https://img.shields.io/discord/925384545342201896?label=discord&style=plastic"></a>\n</p>\n\n## About:\n\nThis package provides a **Multi manager client** which manages **manager** clients.\n\n\n## Usage:\n> ❗NOTE: You need to provide your middleware [access token](https://docs.scramjet.org/platform/quick-start#step-1-set-up-the-environment) if you are not hosting STH locally.\n\n```python\nimport asyncio\nfrom multi_manager_client.multi_manager_client import MultiManagerClient\n\nURL = \'https://api.scp.ovh/api/v1/space/<manager-id>/api/v1/\'\nTOKEN = \'\' # your middleware token\nCONFIG = {\n    \'manager\': {\n        \'id\': \'<manager-id>\'    # manager (hub) id\n    }\n}\n\nmanager = MultiManagerClient(URL, CONFIG, TOKEN)\nres = asyncio.run(manager.get_version())\n```\n',
    'author': 'Scramjet',
    'author_email': 'open-source@scramjet.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
