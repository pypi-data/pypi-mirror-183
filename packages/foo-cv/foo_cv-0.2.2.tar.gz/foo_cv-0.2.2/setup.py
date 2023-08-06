# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['foo_cv']

package_data = \
{'': ['*']}

install_requires = \
['jinja2>=3.1.2,<4.0.0',
 'loguru>=0.6.0,<0.7.0',
 'mistletoe>=0.9.0,<0.10.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['foo-cv = foo_cv.cli:main']}

setup_kwargs = {
    'name': 'foo-cv',
    'version': '0.2.2',
    'description': 'Separate content and style for CV generation',
    'long_description': '# FOO CV\n\n[![codecov](https://codecov.io/gh/drorata/foo-cv/branch/main/graph/badge.svg?token=N44MD6UJ3Z)](https://codecov.io/gh/drorata/foo-cv)\n![PyPI](https://img.shields.io/pypi/v/foo-cv)\n![GitHub](https://img.shields.io/github/license/drorata/foo-cv)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/foo-cv)\n![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/drorata/foo-cv/test_code.yml)\n\n> Separate content and design for CV\n\nWe provide two files:\n- Content given as JSON and\n- a Jinja2 LaTeX template.\n\nThe provided Python script merely connects the two and generates a TeX file that can then be processed using PDFLaTeX.\n\n[`json_resume`](https://github.com/prat0318/json_resume) is the main source of inspiration for this.\n\n## The profile picture\n\nThe [picture](./profile-pic.jpg) was created using [Dalle](https://labs.openai.com/) given the description:\n\n> Create a portrait of Elrond mixed with Worf\n',
    'author': 'Dror Atariah',
    'author_email': 'drorata@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/drorata/foo-cv',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
