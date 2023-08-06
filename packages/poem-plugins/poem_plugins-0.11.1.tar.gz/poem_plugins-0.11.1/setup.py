# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poem_plugins',
 'poem_plugins.general',
 'poem_plugins.general.version_driver',
 'poem_plugins.versions']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2,<2.0']

entry_points = \
{'poetry.plugin': ['poem-git-long-version-plugin = '
                   'poem_plugins.versions.git:GitLongVersionPlugin']}

setup_kwargs = {
    'name': 'poem-plugins',
    'version': '0.11.1',
    'description': 'Some set of poetry plugins',
    'long_description': '# Poem Plugins\n\n<a href="https://pypi.org/project/poem-plugins" target="_blank">\n    <img src="https://img.shields.io/pypi/v/poem-plugins?color=%2334D058&label=pypi%20package" alt="Package version">\n</a>\n\nA set of plugins for [**Poetry**](https://python-poetry.org/).\n\n\n## How to use\nMake sure you have Poetry version `1.2.0` or above. Read below for instructions to install it if you haven\'t.\n\n### Install Poem Plugins\n\nInstall this plugin to your Poetry:\n\n```console\n$ poetry self add poem-plugins\n```\n\nAdd tool section in project pyproject.toml\n\n```toml\n[tool.poem-plugins]\nversion_plugin = "git-long"\n# Version tags must be starts with this prefix\ngit_version_prefix = "v"\n```\n\nCreate a git tag, for example:\n\n```console\n$ git tag v0.1\n```\n\nNext, build your project. It will show an output like:\n\n```console\n$ poetry build\npoem-plugins: Setting version to: 0.1.0+g5ee9240\nBuilding awesome_package (0.1.0+g5ee9240)\n  - Building sdist\n  - Built awesome_package-0.1.0+g5ee9240.tar.gz\n  - Building wheel\n  - Built awesome_package-0.1.0+g5ee9240-py3-none-any.whl```\n```\n',
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
