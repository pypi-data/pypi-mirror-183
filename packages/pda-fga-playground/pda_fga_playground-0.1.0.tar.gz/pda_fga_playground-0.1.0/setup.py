# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['src',
 'src.data_treatment',
 'src.data_treatment.data_pre_processing',
 'src.parser',
 'src.parser.feature_engineering',
 'src.parser.initial',
 'src.parser.initial.tests',
 'src.parser.tests']

package_data = \
{'': ['*'],
 'src': ['yamls/*'],
 'src.parser.initial.tests': ['mock/*'],
 'src.parser.tests': ['mock/*',
                      'mock/first_case/*',
                      'mock/second_case/*',
                      'mock/third_case/*']}

install_requires = \
['pandas>=1.5.2,<2.0.0',
 'pytest-cov>=4.0.0,<5.0.0',
 'pytest>=7.2.0,<8.0.0',
 'pyyaml>=6.0,<7.0']

setup_kwargs = {
    'name': 'pda-fga-playground',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Playground',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
