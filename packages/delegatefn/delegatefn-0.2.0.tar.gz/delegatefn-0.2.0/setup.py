# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['delegatefn']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'delegatefn',
    'version': '0.2.0',
    'description': 'Signature-preserving function delegation',
    'long_description': 'A tiny utility for preserving signature information (parameter names, annotations, and docstrings) when delegating one\nfunction to another.\n\nWorks for keyword arguments only; positional arguments are not supported.\n\n# Installation\n\n```bash\npip install delegatefn\n```\n\n# Usage\n\n```python\nfrom delegatefn import delegate\nimport inspect\n\ndef foo(a, b, c):\n    """This is the docstring for foo."""\n\n@delegate(foo)\ndef bar(**kwargs):\n    """This is the docstring for bar."""\n\nassert foo.__doc__ == bar.__doc__ == "This is the docstring for foo."\nassert inspect.signature(bar).parameters.keys() == {"a", "b", "c"}\n```\n\n# Limitations\n\nUnfortunately, there isn\'t an easy way to combine docstrings from multiple functions. Instead, `delegate` lets you\ndecide which function\'s docstring to use.\n\n```python\nfrom delegatefn import delegate\n\ndef foo(a, b, c):\n    """This is the docstring for foo."""\n\n@delegate(foo, delegate_docstring=False)\ndef bar(**kwargs):\n    """This is the docstring for bar."""\n\nassert foo.__doc__ != bar.__doc__ == "This is the docstring for bar."\n```\n\n# Acknowledgements\n\nThis approach was inspired by [fast.ai](https://www.fast.ai/posts/2019-08-06-delegation.html).',
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
