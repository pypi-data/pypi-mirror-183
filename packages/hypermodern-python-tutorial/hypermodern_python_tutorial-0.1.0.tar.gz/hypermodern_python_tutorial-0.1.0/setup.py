# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['hypermodern_python_tutorial']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'desert>=2022.9.22,<2023.0.0',
 'marshmallow>=3.19.0,<4.0.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['hypermodern-python-tutorial = '
                     'hypermodern_python_tutorial.console:main']}

setup_kwargs = {
    'name': 'hypermodern-python-tutorial',
    'version': '0.1.0',
    'description': 'The hypermodern Python project',
    'long_description': '![Tests](https://github.com/prometeyqwe/hypermodern-python-tutorial/actions/workflows/tests.yml/badge.svg)\n[![codecov](https://codecov.io/gh/prometeyqwe/hypermodern-python-tutorial/branch/main/graph/badge.svg?token=LHZW5RGLMV)](https://codecov.io/gh/prometeyqwe/hypermodern-python-tutorial)\n\nhypermodern-python-tutorial\n',
    'author': 'Evgeny Kirillov',
    'author_email': 'kirilllov.evgeny@mail.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/prometeyqwe/hypermodern-python-tutorial',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
