# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['font_fjallaone']

package_data = \
{'': ['*'], 'font_fjallaone': ['files/*']}

entry_points = \
{'fonts_ttf': ['fjallaone = font_fjallaone:font_files']}

setup_kwargs = {
    'name': 'font-fjallaone',
    'version': '0.1.1',
    'description': 'Fjalla One from from Sorkin Type as distributed by Google Fonts',
    'long_description': 'None',
    'author': 'IT-Reaktion',
    'author_email': 'it@rabe.ch',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
