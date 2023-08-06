# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['software_engineer_assignment']

package_data = \
{'': ['*']}

install_requires = \
['pyqt5>=5.15.7,<6.0.0', 'pyqtgraph>=0.13.1,<0.14.0', 'pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'software-engineer-assignment0-1',
    'version': '1.0.0',
    'description': 'Software Engineering assignment for job interview.',
    'long_description': 'Software Engineering Assignment\n\n\n',
    'author': 'MartinP96',
    'author_email': 'porenta.martin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
