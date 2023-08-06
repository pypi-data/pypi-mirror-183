# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tests', 'tests.unit']

package_data = \
{'': ['*']}

modules = \
['treestamps']
install_requires = \
['bandit>=1.7.4,<2.0.0',
 'flake8-eradicate>=1.4.0,<2.0.0',
 'ruamel.yaml>=0.17.21,<0.18.0',
 'termcolor>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'treestamps',
    'version': '0.3.3',
    'description': 'Create timestamp records for recursive operations on directory trees.',
    'long_description': '# Treestamps\n\nA library to set and retrieve timestamps to speed up operations\nrun recursively on directory trees.\n\nPrincipal methods on the Treestamps class are: init(), get(), set(), dump().\nA factory method is also provided for creating top path to Treestamp maps.\n\nDocumentation is to read the code for now.\n',
    'author': 'AJ Slater',
    'author_email': 'aj@slater.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ajslater/treestamps',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
