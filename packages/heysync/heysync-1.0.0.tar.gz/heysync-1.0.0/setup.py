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
    'version': '1.0.0',
    'description': 'Hey, make async functions and classes sync',
    'long_description': '# Hey, Sync!\n\nThis package will allow you to convert an async function or a class (that has async methods) to a sync version.  \nThe new class name will be set as `<OLD CLASS NAME>Sync`\n',
    'author': 'oren0e',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
