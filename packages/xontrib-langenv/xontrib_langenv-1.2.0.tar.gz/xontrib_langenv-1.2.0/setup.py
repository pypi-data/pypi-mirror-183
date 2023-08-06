# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xontrib']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xontrib-langenv',
    'version': '1.2.0',
    'description': 'Pyenv/Nodenv/Goenv/Rbenv integration for xonsh',
    'long_description': '# xontrib-langenv\n\n[xonsh](https://xon.sh) integration with:\n\n* [Pyenv](https://github.com/pyenv/pyenv)\n* [Nodenv](https://github.com/nodenv/nodenv)\n* [Goenv](https://github.com/syndbg/goenv)\n* [Rbenv](https://github.com/rbenv/rbenv)\n\n## Install\n\nInstall using pip\n\n```\npip install xontrib-langenv\n```\n\n## Usage\n\nAdd to your `.xonshrc` as follows:\n\n### Pyenv\n\n```sh\nxontrib load pyenv\n```\n\nThis xontrib initializes `pyenv` when `xonsh` is started.\nAfter initialization `pyenv` commands works as they would do in any *classic* shell.\n\nAlso supports [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).\n\n### Nodenv\n\n```sh\nxontrib load nodenv\n```\n\nThis xontrib initializes `nodenv` when `xonsh` is started.\nAfter initialization `nodenv` commands works as they would do in any *classic* shell.\n\n### Goenv\n\n```sh\nxontrib load goenv\n```\n\nThis xontrib initializes `goenv` when `xonsh` is started.\nAfter initialization `goenv` commands works as they would do in any *classic* shell.\n\n### Rbenv\n\n```sh\nxontrib load rbenv\n```\n\nThis xontrib initializes `rbenv` when `xonsh` is started.\nAfter initialization `rbenv` commands works as they would do in any *classic* shell.\n\n## Compatibility notes\n\nIf you are using `xonsh` v0.11 (or older) and you have issues with the latest version of this xontrib, try to downgrade it to version 1.0.6.\n',
    'author': 'Gyuri Horak',
    'author_email': 'dyuri@horak.hu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dyuri/xontrib-langenv',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
