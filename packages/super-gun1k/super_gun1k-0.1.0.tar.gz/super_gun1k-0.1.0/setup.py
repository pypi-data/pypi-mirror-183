# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['super_gun1k']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['super = super_gun1k.main:app']}

setup_kwargs = {
    'name': 'super-gun1k',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Super Gun 1000\n\n\nSimple app to push to learn how to push to PyPi!\n',
    'author': 'evan',
    'author_email': 'evan@pop-os.localdomain',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
