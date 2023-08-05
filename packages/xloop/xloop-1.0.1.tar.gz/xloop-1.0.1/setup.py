# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xloop']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'xloop',
    'version': '1.0.1',
    'description': 'General purpose for/iterator looping generators/utilities.',
    'long_description': '![PythonSupport](https://img.shields.io/static/v1?label=python&message=%203.8|%203.9|%203.10|%203.11&color=blue?style=flat-square&logo=python)\n![PyPI version](https://badge.fury.io/py/xloop.svg?)\n\n- [Introduction](#introduction)\n- [Documentation](#documentation)\n- [Install](#install)\n- [Quick Start](#quick-start)\n- [Licensing](#licensing)\n\n# Introduction\n\nThis library is intended to house general for/iterator looping generators/utilities.\n\nOnly one so far is `xloop`, see **[xloop docs](https://xyngular.github.io/py-xloop/latest/)**.\n\n# Documentation\n\n**[📄 Detailed Documentation](https://xyngular.github.io/py-xloop/latest/)** | **[🐍 PyPi](https://pypi.org/project/xloop/)**\n\n# Install\n\n```bash\n# via pip\npip install xloop\n\n# via poetry\npoetry add xloop\n```\n\n# Quick Start\n\n```python\nfrom xloop import xloop\n\nargs = [None, "hello", 2, [3, 4], [\'A\', ["inner", "list"]]]\n\noutput = list(xloop(*args))\n\nassert output == ["hello", 2, 3, 4, \'A\', ["inner", "list"]]\n```\n\n\n\n# Licensing\n\nThis library is licensed under the MIT-0 License. See the LICENSE file.\n',
    'author': 'Josh Orr',
    'author_email': 'josh@orr.blue',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xyngular/py-xloop',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
