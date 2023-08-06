# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cd_dynamic_versioning']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cd-dynamic-versioning',
    'version': '0.0.2',
    'description': 'Testpackage for dynamic versioning',
    'long_description': '# Continuous delivery with dynamic versioning\n\nSkeleton package to demonstrate continuous delivery and dynamic versioning with Poetry and GitHub Actions.',
    'author': 'Yngve Moe',
    'author_email': 'yngve.m.moe@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8.1,<4.0',
}


setup(**setup_kwargs)
