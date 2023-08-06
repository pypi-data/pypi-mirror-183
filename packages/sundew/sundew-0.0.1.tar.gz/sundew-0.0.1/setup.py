# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sundew']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0', 'typer[all]>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'sundew',
    'version': '0.0.1',
    'description': '',
    'long_description': '# sundew ☀️\nA new kind of testing framework for Python.\n\n> **Warning**\n> This projct is barely even a proof-of-concept still and is not close to being ready for production use. This warning will be updated/removed when that has changed!\n\n## To-do\nMajor things that still need to be done before making public (in rough order):\n[x] - Handle test failures\n[ ] - Handle test errors\n[ ] - Fixtures\n[ ] - Write tests for sundew 🤭\n[ ] - Figure out test naming\n[ ] - Basic test selection support\n[ ] - Asyncio support/examples\n[ ] - Documentation\n[ ] - Implement smart test runner\n[ ] - Implement automatic sub-function test cases\n[ ] - Implement untested sub-function detection\n[ ] - Parallel test runner support\n[ ] - Add code of conduct\n[ ] - Add contribution guidelines\n[ ] - Setup Github Actions to release new versions to PyPi\n[ ] - Release first version to Pypi',
    'author': 'devenjarvis',
    'author_email': 'devenjarvis@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
