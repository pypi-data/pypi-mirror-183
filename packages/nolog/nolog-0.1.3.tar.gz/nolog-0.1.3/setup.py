# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nolog', 'nolog.logic_engine', 'nolog.tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'nolog',
    'version': '0.1.3',
    'description': 'A native Logic engine for Python',
    'long_description': '# NoLog\n\nA propositional logic implementation in Python, to be used as a rule engine.',
    'author': 'Dragos Dumitrache',
    'author_email': 'dragos@afterburner.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
