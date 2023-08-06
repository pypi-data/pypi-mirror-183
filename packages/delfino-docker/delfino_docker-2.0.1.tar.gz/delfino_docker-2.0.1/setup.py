# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['delfino_docker']

package_data = \
{'': ['*']}

install_requires = \
['delfino>=1.1.0,<2.0.0', 'packaging>=22.0,<23.0']

entry_points = \
{'delfino.plugin': ['delfino-docker = delfino_docker']}

setup_kwargs = {
    'name': 'delfino-docker',
    'version': '2.0.1',
    'description': 'A delfino plugin with helper scripts for working with docker.',
    'long_description': '<h1 align="center" style="border-bottom: none;"> 🔌&nbsp;&nbsp;Delfino Docker&nbsp;&nbsp; 🔌</h1>\n<h3 align="center">A delfino plugin with helper scripts for working with docker.</h3>\n\n<p align="center">\n    <a href="https://app.circleci.com/pipelines/github/radeklat/delfino-docker?branch=main">\n        <img alt="CircleCI" src="https://img.shields.io/circleci/build/github/radeklat/delfino-docker">\n    </a>\n    <a href="https://app.codecov.io/gh/radeklat/delfino-docker/">\n        <img alt="Codecov" src="https://img.shields.io/codecov/c/github/radeklat/delfino-docker">\n    </a>\n    <a href="https://github.com/radeklat/delfino-docker/tags">\n        <img alt="GitHub tag (latest SemVer)" src="https://img.shields.io/github/tag/radeklat/delfino-docker">\n    </a>\n    <img alt="Maintenance" src="https://img.shields.io/maintenance/yes/2022">\n    <a href="https://github.com/radeklat/delfino-docker/commits/main">\n        <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/radeklat/delfino-docker">\n    </a>\n    <a href="https://www.python.org/doc/versions/">\n        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/delfino-docker">\n    </a>\n    <a href="https://pypistats.org/packages/delfino-docker">\n        <img alt="Downloads" src="https://img.shields.io/pypi/dm/delfino-docker">\n    </a>\n</p>\n\n# Commands\n  \n| Command      | Description                                                                              |\n|--------------|------------------------------------------------------------------------------------------|\n| docker-build | Runs a `docker build` command for multiple platforms and pushes to dockerhub at the end. |\n\n# Installation\n\n- pip: `pip install delfino-docker`\n- Poetry: `poetry add -D delfino-docker`\n- Pipenv: `pipenv install -d delfino-docker`\n\n<!-- PUT DEPENDENCIES OF INDIVIDUAL COMMANDS AS EXTRAS -->\n<!--\n## Optional dependencies\n\nEach project may use different sub-set of [commands](#commands). Therefore, dependencies of all commands are optional and checked only when the command is executed.\n\nUsing `[all]` installs all the [optional dependencies](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies) used by all the commands. If you want only a sub-set of those dependencies, there are finer-grained groups available:\n\n- `demo`\n-->\n\n# Configuration\n\nDelfino doesn\'t load any plugins by default. To enable this plugin, add the following config into `pyproject.toml`:\n\n```toml\n[tool.delfino.plugins.delfino-docker]\n\n```\n\n<!-- PLUGIN MAY NEED CONFIGURATION -->\n<!--\n## Plugin configuration\n\nThis plugin has several options. All the values are optional and defaults are shown below: \n\n```toml\n[tool.delfino.plugins.delfino-docker]\n# Config option description\nconfig_option_name = "default value"\n```\n-->\n\n## Commands configuration\n\n```toml\n[tool.delfino.plugins.delfino-docker.docker-build]\n# User name for logging in into dockerhub\ndockerhub_username = ""\n\n# Platforms to build with dockerx\nbuild_for_platforms = [\n    "linux/arm/v7",\n    "linux/arm64",\n    "linux/amd64",\n]\n```\n\n# Usage\n\nRun `delfino --help`.\n',
    'author': 'Radek Lat',
    'author_email': 'radek.lat@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/radeklat/delfino-docker',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2,<=3.11',
}


setup(**setup_kwargs)
