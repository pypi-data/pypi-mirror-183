# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gr_trading']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['gr = gr_trading.gr:gr']}

setup_kwargs = {
    'name': 'gr-trading',
    'version': '0.3',
    'description': 'Comandos para cálculos de gerenciamento de risco no trading',
    'long_description': '# gr-trading\n\nComandos para cálculos de gerenciamento de risco no trading\n\n\n',
    'author': 'Valmir Franca',
    'author_email': 'vfranca3@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/vfranca/gr-trading',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
