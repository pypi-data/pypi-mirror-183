# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qis',
 'qis.data',
 'qis.examples',
 'qis.models',
 'qis.models.linear',
 'qis.models.ml',
 'qis.models.stats',
 'qis.perfstats',
 'qis.plots',
 'qis.plots.derived',
 'qis.portfolio',
 'qis.portfolio.optimization',
 'qis.portfolio.reports',
 'qis.portfolio.strats',
 'qis.utils',
 'qis.utils.generic']

package_data = \
{'': ['*'], 'qis': ['resources/*', 'resources/xml/*']}

install_requires = \
['matplotlib>=3.5.2',
 'numba>=0.55',
 'numpy>=1.22.4',
 'pandas>=0.19',
 'scipy>=1.3',
 'seaborn>=0.11.2',
 'statsmodels>=0.13.0']

setup_kwargs = {
    'name': 'qis',
    'version': '1.0.3',
    'description': 'Implementation of visualisation and reporting analytics for Quantitative Investment Strategies',
    'long_description': '# READ ME\n\n## **Analytics**\n\nTO DO\n\n\n',
    'author': 'Artur Sepp',
    'author_email': 'artursepp@gmail.com',
    'maintainer': 'Artur Sepp',
    'maintainer_email': 'artursepp@gmail.com',
    'url': 'https://github.com/ArturSepp/QuantInvestStrats',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
