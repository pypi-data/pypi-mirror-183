# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['proxyx']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.1,<0.24.0',
 'pydantic-yaml>=0.8.1,<0.9.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'starlette>=0.23.1,<0.24.0',
 'uvicorn>=0.20.0,<0.21.0']

extras_require = \
{'sentry-sdk': ['sentry-sdk>=1.12.1,<2.0.0']}

setup_kwargs = {
    'name': 'proxyx',
    'version': '0.0.2',
    'description': 'A very simple proxy server that just works.',
    'long_description': '# proxyx\n\nA very simple proxy server that just works.\n\ntodo:\n- docker image\n- cache handling (limiter and cache response)\n- compare with nginx most often used\n- request size\n- add tests\n- add a few examples\n- handle favicon\n-\n',
    'author': 'Tom Wojcik',
    'author_email': 'proxyx-pkg@tomwojcik.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tomwojcik/proxyx',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
