# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poem_plugins',
 'poem_plugins.config',
 'poem_plugins.dispatchers',
 'poem_plugins.general',
 'poem_plugins.general.version',
 'poem_plugins.general.version.drivers',
 'poem_plugins.plugins']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2,<2.0']

entry_points = \
{'poetry.application.plugin': ['poem-version-plugin = '
                               'poem_plugins.plugins:VersionPlugin']}

setup_kwargs = {
    'name': 'poem-plugins',
    'version': '0.14.0.dev1',
    'description': 'Some set of poetry plugins',
    'long_description': '# Poem Plugins\n\n[![Pypi](https://img.shields.io/pypi/v/poem-plugins?color=%2334D058&label=pypi%20package)](https://pypi.org/project/poem-plugins)\n[![Coverage Status](https://coveralls.io/repos/github/Alviner/poem-plugins/badge.svg?branch=main)](https://coveralls.io/github/Alviner/poem-plugins?branch=main)\n\nA set of plugins for [**Poetry**](https://python-poetry.org/).\n\n## How to use\nMake sure you have Poetry version `1.2.0` or above. Read below for instructions to install it if you haven\'t.\n\n### Install Poem Plugins\n\nInstall this plugin to your Poetry:\n\n```console\n$ poetry self add poem-plugins\n```\n\nAdd tool section in project pyproject.toml\n\n```toml\n[tool.poem-plugins.version]\nprovider = "git"\n# Create a file with version inside a project, default: false\nwrite_version_file = true\n# Save new version on pyproject, default: false\nupdate_pyproject = true\n\n\n[tool.poem-plugins.version.git]\n# Version tags must be starts with this prefix, default: \'v\'\nversion_prefix = "v"\n# Version format with commit hash (long) or not (short), default: \'short\'\nformat = "short"\n```\n\nCreate a git tag, for example:\n\n```console\n$ git tag v0.1\n```\n\nNext, build your project. It will show an output like:\n\n```console\n$ poetry build\npoem-plugins: Setting version to: 0.1.0\nBuilding awesome_package (0.1.0)\n  - Building sdist\n  - Built awesome_package-0.1.0.tar.gz\n  - Building wheel\n  - Built awesome_package-0.1.0-py3-none-any.whl```\n```\n',
    'author': 'Ivan Sitkin',
    'author_email': 'alvinera@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/poem-plugins',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
