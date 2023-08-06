# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tomlenv']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tomlenv',
    'version': '0.2.1',
    'description': 'Environment Wrapped TOML',
    'long_description': '# TOMLenv\n![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/joaonsantos/tomlenv/python-publish.yml)\n![PyPI - Version](https://img.shields.io/pypi/v/tomlenv)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tomlenv)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/tomlenv)\n![License](https://img.shields.io/github/license/joaonsantos/tomlenv)\n\nEnvironment wrapped TOML.\n\n## Getting Started\n\n### Install the library\n\nUsing pip:\n```sh\n$ pip install tomlenv\n```\n\nUsing pipenv:\n```sh\n$ pipenv install tomlenv\n```\n\nUsing poetry:\n```sh\n$ poetry add tomlenv\n```\n\n### Basic Usage\n\nAssuming you have a `config.toml` file in your project root:\n```toml\ntoken = "dev"\ndebug = false\n```\n\nAnd this environment set:\n```sh\nTOMLENV_DEBUG=true\n```\n\nCreate your configuration dataclass and parse configuration into it:\n```python\nimport tomlenv\n\nclass Config:\n    token: str = ""\n    enabled: bool = False\n\nconfig = Config()\nparser = tomlenv.Parser()\n\nparser.load(config)\n\n# You can now access the fields of your fully typed Config class\n# that contains values from a TOML config file and the environment.\n#\n# For example:\n\ntoken = config.token\ndebug = config.debug\nprint(token) # prints "dev"\nprint(debug) # prints True\n```\n\n## Configuration\n\nTo configure the location of your toml file, set `TOMLENV_CONF_FILEPATH`.\n\nFor example if your config file is in `configs/config.toml` relative to the project root, then set `TOMLENV_CONF_FILEPATH=configs/config.toml`\n\n## Tests\n\nThis project uses [Poetry](https://python-poetry.org/) and [GNU Make](https://www.gnu.org/software/make/).\n\nRun tests from the project root with:\n```sh\n$ make test\n```\n\nTo get a coverage report:\n```sh\n$ make cov\n```',
    'author': 'João Santos',
    'author_email': 'joaopns05@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/joaonsantos/tomlenv',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
