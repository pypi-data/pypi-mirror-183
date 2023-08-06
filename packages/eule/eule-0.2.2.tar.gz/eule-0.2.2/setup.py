# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src', 'src.examples']

package_data = \
{'': ['*']}

install_requires = \
['coverage>=7.0,<8.0',
 'isort>=5.11.4,<6.0.0',
 'numpy>=1.24.1,<2.0.0',
 'sphinx>=5.3.0,<6.0.0',
 'sphinxcontrib-serializinghtml>=1.1.5,<2.0.0',
 'sphinxcontrib-websupport>=1.2.4,<2.0.0',
 'tox>=4.0.19,<5.0.0',
 'watchdog>=2.2.0,<3.0.0',
 'wheel>=0.38.4,<0.39.0']

setup_kwargs = {
    'name': 'eule',
    'version': '0.2.2',
    'description': 'Euler diagrams in python',
    'long_description': '![a night owl](https://raw.githubusercontent.com/quivero/eule/main/images/eule_small.png)\n\n[![Version](https://img.shields.io/pypi/v/eule.svg)](https://pypi.python.org/pypi/eule)\n[![python](https://img.shields.io/pypi/pyversions/eule.svg)](https://pypi.org/project/eule/)\n[![Documentation Status](https://readthedocs.org/projects/eule/badge/?version=latest)](https://eule.readthedocs.io/en/latest/?version=latest)\n\n[![codecov](https://codecov.io/gh/quivero/eule/branch/main/graph/badge.svg?token=PJMBaLIqar)](https://codecov.io/gh/quivero/eule)\n[![Codecov workflow](https://github.com/quivero/eule/actions/workflows/test-coverage.yml/badge.svg)](https://github.com/quivero/eule/actions/workflows/test-coverage.yml)\n[![Lint workflow](https://github.com/quivero/eule/actions/workflows/check-lint.yaml/badge.svg)](https://github.com/quivero/eule/actions/workflows/check-lint.yaml)\n[![downloads](https://img.shields.io/pypi/dm/eule)](https://pypi.org/project/eule/)\n\n\nEuler\\\'s diagrams are non-empty Venn\\\'s diagrams. For further information about:\n\n1. the library: read the documentation on URL <https://eule.readthedocs.io>;\n2. Euler diagrams: read the wikipedia article <https://en.wikipedia.org/wiki/Euler_diagram>\n\nMotivation\n================\n\n<img src="https://github.com/quivero/eule/blob/main/images/euler_venn.png?raw=true" width="400" height="364"/>\n\nHow to install\n================\n\nWe run the command on desired installation environment:\n\n``` {.bash}\n    pip install eule\n```\n\nMinimal example\n================\n\nWe run a file with extension `*.py` with following content:\n\n``` {.python}\n#!/usr/bin/env python\nfrom eule import spread_euler\n\nset = {\n    \'a\': [1, 2, 3],\n    \'b\': [2, 3, 4],\n    \'c\': [3, 4, 5],\n    \'d\': [3, 5, 6]\n}\n\ndiagram = spread_euler(set)\n\n# Euler dictionary: {\'a,b\': [2], \'b,c\': [4], \'a,b,c,d\': [3], \'c,d\': [5], \'d\': [6], \'a\': [1]}\nprint(diagram)\n```\n\nLicense\n===============\n\n-   Free software: MIT license\n\n\nCredits\n===============\n\nThis package was created with\n[Cookiecutter](https://github.com/audreyr/cookiecutter) and the\n[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)\nproject template.\n',
    'author': 'Bruno Peixoto',
    'author_email': 'brunolnetto@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/eule/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
