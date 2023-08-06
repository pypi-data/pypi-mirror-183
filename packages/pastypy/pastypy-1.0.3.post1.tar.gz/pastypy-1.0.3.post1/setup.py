# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pastypy']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0',
 'pycryptodome>=3.14.1,<4.0.0',
 'requests>=2.27.1,<3.0.0',
 'tomli>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'pastypy',
    'version': '1.0.3.post1',
    'description': 'Pasty API wrapper',
    'long_description': '# PastyPY\n\n[![pytest](https://github.com/zevaryx/pastypy/actions/workflows/pytest.yml/badge.svg)](https://github.com/zevaryx/pastypy/actions/workflows/pytest.yml) [![codecov](https://codecov.io/gh/zevaryx/pastypy/branch/main/graph/badge.svg?token=IPC1OMI36K)](https://codecov.io/gh/zevaryx/pastypy)\n\nA Python wrapper around [Pasty](https://github.com/lus/pasty) written by lus\n\n## Features\n\n- Full API coverage\n- `asyncio` support with `pastypy.AsyncPaste`\n- Encryption support\n\n## Examples\n\nSee [examples](https://github.com/zevaryx/pastypy/tree/main/examples) for usage and examples\n',
    'author': 'Zevaryx',
    'author_email': 'zevaryx@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/zevaryx/pastypy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4',
}


setup(**setup_kwargs)
