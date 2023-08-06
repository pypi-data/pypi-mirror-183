# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['heysync']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'heysync',
    'version': '1.0.1',
    'description': 'Hey, make async functions and classes sync',
    'long_description': '# Hey, Sync!\n\nThis package will allow you to convert an async function or a class (that has async methods) to a sync version.  \nThe new class name will be set as `<OLD CLASS NAME>Sync`\n\n## Installation\n\n`pip install heysync`\n\n## Usage\n\n### Async Functions\n\nYou can convert async functions to sync function by:\n\n1. Normal usage:\n\n```python\nfrom heysync import async_to_sync_func\n\nasync def async_func() -> str:\n    return "Hey there"\n\nsync_func = async_to_sync_func(async_func)\n\n# now you can call sync_func in the usual way\nsync_func()  # Hey there\n```\n\n2. As a decorator:\n\n```python\nfrom heysync import async_to_sync_func\n\n@async_to_sync_func\nasync def some_func() -> str:\n    return "boo"\n\nsome_func()  # boo\n```\n\n### Classes\n\nYou can also convert async classes:\n\n```python\nfrom heysync import make_sync_class\n\n# a class with async methods\nclass Foo:\n    def __init__(self, x: int) -> None:\n        self.x = x\n\n    async def __aenter__(self):\n        self.x += 2\n        await async_func()\n        return self\n\n    async def __aexit__(self, exc_type, exc_value, exc_tb) -> None:\n        self.x -= 1\n        await async_func()\n\n    async def my_func(self) -> str:\n        return f"Output is {self.x}"\n\nFooSync = make_sync_class(Foo)\nwith Foo(7) as foo:\n    foo.my_func()  # Output is 9\nfoo.my_func()  # Output is 8\n```\n',
    'author': 'oren0e',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/oren0e/heysync',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
