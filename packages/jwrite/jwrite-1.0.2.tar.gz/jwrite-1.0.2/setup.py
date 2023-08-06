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
    'version': '1.0.2',
    'description': 'Notepad clone made with PySide6',
    'long_description': '# jwrite\n\n![GPL-3.0 License](https://img.shields.io/github/license/jrrom/jwrite)\n![100% Python, except the parts not shown here](https://img.shields.io/github/languages/top/jrrom/jwrite)\n![Version](https://img.shields.io/pypi/v/jwrite)\n![Supports Python 3.7, 3.8, 3.9, 3.10 and 3.11](https://img.shields.io/pypi/pyversions/jwrite)\n\n## About -\n\nThis is a minimal notepad clone made to learn [PySide6](https://doc.qt.io/qtforpython/index.html) for a school project. It uses QUI files for structuring its main components.\nDownload the package using `pip install jwrite` or `pip3 install jwrite`\n\n## Showcase -\nVideo - https://youtu.be/YS1AV7d7t88\n\n![New Screen](https://user-images.githubusercontent.com/77691121/209984324-055cfa72-f1dd-4d82-9594-d86b559e3ce5.png)\n![Some text selected](https://user-images.githubusercontent.com/77691121/209984428-f2fb929d-bd84-49cf-89cc-3cde30bea61d.png)\n![About Page](https://user-images.githubusercontent.com/77691121/209984573-59ed67d0-6a6a-44b7-b23a-eb5107a9a70f.png)\n',
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
