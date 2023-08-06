# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simplipy',
 'simplipy.device',
 'simplipy.device.sensor',
 'simplipy.system',
 'simplipy.util']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.0',
 'backoff>=1.11.1',
 'beautifulsoup4>=4.11.1',
 'pytz>=2019.3',
 'voluptuous>=0.11.7',
 'websockets>=8.1']

setup_kwargs = {
    'name': 'simplisafe-python',
    'version': '2022.12.1',
    'description': 'A Python3, async interface to the SimpliSafe API',
    'long_description': '# 🚨 simplisafe-python: A Python3, async interface to the SimpliSafe™ API\n\n[![CI][ci-badge]][ci]\n[![PyPI][pypi-badge]][pypi]\n[![Version][version-badge]][version]\n[![License][license-badge]][license]\n[![Code Coverage][codecov-badge]][codecov]\n[![Maintainability][maintainability-badge]][maintainability]\n\n<a href="https://www.buymeacoffee.com/bachya1208P" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>\n\n`simplisafe-python` (hereafter referred to as `simplipy`) is a Python3,\n`asyncio`-driven interface to the unofficial [SimpliSafe™][simplisafe] API. With it,\nusers can get data on their system (including available sensors), set the system state,\nand more.\n\n# Documentation\n\nYou can find complete documentation [here][docs].\n\n# Contributing\n\nThanks to all of [our contributors][contributors] so far!\n\n1. [Check for open features/bugs][issues] or [initiate a discussion on one][new-issue].\n2. [Fork the repository][fork].\n3. (_optional, but highly recommended_) Create a virtual environment: `python3 -m venv .venv`\n4. (_optional, but highly recommended_) Enter the virtual environment: `source ./.venv/bin/activate`\n5. Install the dev environment: `script/setup`\n6. Code your new feature or bug fix on a new branch.\n7. Write tests that cover your new functionality.\n8. Run tests and ensure 100% code coverage: `poetry run pytest --cov simplisafe-python tests`\n9. Update `README.md` with any new documentation.\n10. Submit a pull request!\n\n[ci-badge]: https://github.com/bachya/simplisafe-python/workflows/CI/badge.svg\n[ci]: https://github.com/bachya/simplisafe-python/actions\n[codecov-badge]: https://codecov.io/gh/bachya/simplisafe-python/branch/dev/graph/badge.svg\n[codecov]: https://codecov.io/gh/bachya/simplisafe-python\n[contributors]: https://github.com/bachya/simplisafe-python/graphs/contributors\n[docs]: https://simplisafe-python.readthedocs.io\n[fork]: https://github.com/bachya/simplisafe-python/fork\n[issues]: https://github.com/bachya/simplisafe-python/issues\n[license-badge]: https://img.shields.io/pypi/l/simplisafe-python.svg\n[license]: https://github.com/bachya/simplisafe-python/blob/main/LICENSE\n[maintainability-badge]: https://api.codeclimate.com/v1/badges/f46d8b1dcfde6a2f683d/maintainability\n[maintainability]: https://codeclimate.com/github/bachya/simplisafe-python/maintainability\n[new-issue]: https://github.com/bachya/simplisafe-python/issues/new\n[pypi-badge]: https://img.shields.io/pypi/v/simplisafe-python.svg\n[pypi]: https://pypi.python.org/pypi/simplisafe-python\n[simplisafe]: https://simplisafe.com\n[version-badge]: https://img.shields.io/pypi/pyversions/simplisafe-python.svg\n[version]: https://pypi.python.org/pypi/simplisafe-python\n',
    'author': 'Aaron Bach',
    'author_email': 'bachya1208@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bachya/simplisafe-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
