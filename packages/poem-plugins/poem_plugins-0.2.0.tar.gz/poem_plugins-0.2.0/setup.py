# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poem_plugins', 'poem_plugins.general', 'poem_plugins.versions']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2,<2.0']

entry_points = \
{'poetry.plugin': ['poem-git-long-version-plugin = '
                   'poem_plugins.versions.git:GitLongVersionPlugin']}

setup_kwargs = {
    'name': 'poem-plugins',
    'version': '0.2.0',
    'description': 'Some set of poetry plugins',
    'long_description': "# Poem Plugins\n\nA set of plugins for [**Poetry**](https://python-poetry.org/).\n\n\n## How to use\nMake sure you have Poetry version `1.2.0` or above. Read below for instructions to install it if you haven't.\n\n### Install Poem Plugins\n\nInstall this plugin to your Poetry:\n\n```console\n$ poetry self add poem-plugins\n```\n",
    'author': 'Ivan Sitkin',
    'author_email': 'alvinera@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alviner/poem-plugins',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
