# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['synctodoist', 'synctodoist.managers', 'synctodoist.models']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.1,<0.24.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0']

setup_kwargs = {
    'name': 'synctodoist',
    'version': '0.2.1',
    'description': 'A Python wrapper for the Todoist Sync API v9',
    'long_description': '# SyncTodoist\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/synctodoist?color=red)\n![PyPI - License](https://img.shields.io/pypi/l/synctodoist?color=blue)\n[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)\n[![mypy: checked](https://img.shields.io/badge/mypy-checked-blue)](http://mypy-lang.org)\n[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)\n[![Tests](https://github.com/gaborschulz/pytodoist/actions/workflows/pytest.yml/badge.svg)](https://github.com/gaborschulz/pytodoist/actions/workflows/pytest.yml)\n[![Coverage](https://raw.githubusercontent.com/gaborschulz/synctodoist/main/coverage.svg)](https://github.com/gaborschulz/synctodoist)\n[![PyPI](https://img.shields.io/pypi/v/synctodoist)](https://pypi.org/project/synctodoist/)\n\n## Summary\n\nA Python client for the Todoist Sync v9 API\n\n## Getting Started\n\nGetting started is quite simple:  \n\n`pip install synctodoist`\n\n## Documentation\n\nThe documentation is available here: https://synctodoist.gaborschulz.com.\n\n## Disclaimer\n\nThis app is not created by, affiliated with, or supported by Doist.\n\n## License\n\nFor licensing details, please, see [LICENSE.md](LICENSE.md)\n\n## Copyright\n\nCopyright Gabor Schulz, 2022',
    'author': 'Gabor Schulz',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gaborschulz/synctodoist',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
