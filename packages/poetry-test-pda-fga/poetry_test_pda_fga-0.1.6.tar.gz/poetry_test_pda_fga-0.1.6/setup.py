# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_test_pda_fga',
 'poetry_test_pda_fga.data_treatment',
 'poetry_test_pda_fga.data_treatment.data_pre_processing',
 'poetry_test_pda_fga.parser',
 'poetry_test_pda_fga.parser.feature_engineering',
 'poetry_test_pda_fga.parser.initial',
 'poetry_test_pda_fga.parser.initial.tests',
 'poetry_test_pda_fga.parser.tests']

package_data = \
{'': ['*'],
 'poetry_test_pda_fga': ['yamls/*'],
 'poetry_test_pda_fga.parser.initial.tests': ['mock/*'],
 'poetry_test_pda_fga.parser.tests': ['mock/*',
                                      'mock/first_case/*',
                                      'mock/second_case/*',
                                      'mock/third_case/*']}

install_requires = \
['pandas>=1.5.2,<2.0.0',
 'pytest-cov>=4.0.0,<5.0.0',
 'pytest>=7.2.0,<8.0.0',
 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['poetry_test_pda_fga-cli = '
                     'poetry_test_pda_fga.cli:funcao_teste']}

setup_kwargs = {
    'name': 'poetry-test-pda-fga',
    'version': '0.1.6',
    'description': '',
    'long_description': '',
    'author': 'Bruno-Felix',
    'author_email': 'balvesfelix@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
