# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_test_pda_fga']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['poetry_test_pda_fga-cli = '
                     'poetry_test_pda_fga.cli:funcao_teste']}

setup_kwargs = {
    'name': 'poetry-test-pda-fga',
    'version': '0.1.2',
    'description': '',
    'long_description': '',
    'author': 'Bruno-Felix',
    'author_email': 'balvesfelix@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
