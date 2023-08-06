# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['delegatefn']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'delegatefn',
    'version': '0.1.0',
    'description': 'Signature-preserving function delegation',
    'long_description': 'A tiny utility for preserving signature information (parameter names, annotations, and docstrings) when delegating one function to another.\n\n# Usage\n\n```python\nfrom delegatefn import delegate\nimport inspect\n\n\ndef foo(a, b, c):\n    """This is the docstring for foo."""\n    pass\n\n\n@delegate(foo)\ndef bar(a, b, c):\n    pass\n\n\nassert inspect.signature(bar) == inspect.signature(foo)\n\nprint(inspect.signature(bar))\n# (a, b, c)\n```',
    'author': 'IsaacBreen',
    'author_email': '57783927+IsaacBreen@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
