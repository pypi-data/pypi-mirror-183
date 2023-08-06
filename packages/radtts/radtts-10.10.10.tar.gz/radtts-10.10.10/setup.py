# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['radtts']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['radtts = radtts.main:main']}

setup_kwargs = {
    'name': 'radtts',
    'version': '10.10.10',
    'description': 'Project description',
    'long_description': '# radtts\n',
    'author': 'Tadeusz Miszczyk',
    'author_email': '42252259+8tm@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
