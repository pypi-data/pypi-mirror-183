# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['astea']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'astea',
    'version': '1.0',
    'description': 'A simple python based code traversal engine built with AST',
    'long_description': '# astea\n\nSimple python AST engine with lazy lookup and code traversal\n',
    'author': 'yashbonde',
    'author_email': 'bonde.yash97@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/yashbonde/astea',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
