# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ptmpdy']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'rich>=12.6.0,<13.0.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['ptmpdy = ptmpdy.main:app']}

setup_kwargs = {
    'name': 'ptmpdy',
    'version': '0.1.0',
    'description': '',
    'long_description': '# ptmpdy \n\n"ptmpdy" is "Please Tell Me Path Declaration in Yaml"',
    'author': 'hayata-yamamoto',
    'author_email': 'hayata.yamamoto.work@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
