# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jwrite']

package_data = \
{'': ['*'], 'jwrite': ['views/*']}

install_requires = \
['pyside6>=6.4.1,<7.0.0']

entry_points = \
{'console_scripts': ['jwrite = jwrite:main']}

setup_kwargs = {
    'name': 'jwrite',
    'version': '1.0.0',
    'description': 'Notepad clone made with PySide6',
    'long_description': '# jwrite\n\n## About -\n\nThis is a minimal notepad clone made to learn [PySide6](https://doc.qt.io/qtforpython/index.html) for a school project. It uses QUI files for structuring its main components.',
    'author': 'jrrom',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jrrom/jwrite',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)
