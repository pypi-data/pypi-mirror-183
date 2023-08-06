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
    'version': '0.1.2',
    'description': 'Fjalla One from from Sorkin Type as distributed by Google Fonts',
    'long_description': "# Python Package with Fjalla One Font\n\nPython Package with [Fjalla One](https://fonts.google.com/specimen/Fjalla+One) from\n[Sorkin Type](https://github.com/pimoroni/fonts-python) as distributed by\n[Google Fonts](https://fonts.google.com) for use with\n[fonts-python](https://github.com/pimoroni/fonts-python).\n\n## Installation\n\n```bash\npip install font_fjallaone\n```\n\n## Usage\n\n```python\nfrom font_fjallaone import FjallaOne\n```\n\n## Release Management\n\nThe CI/CD setup uses semantic commit messages following the [conventional commits standard](https://www.conventionalcommits.org/en/v1.0.0/).\nThere is a GitHub Action in [.github/workflows/semantic-release.yaml](./.github/workflows/semantic-release.yaml)\nthat uses [go-semantic-commit](https://go-semantic-release.xyz/) to create new\nreleases.\n\nThe commit message should be structured as follows:\n\n```\n<type>[optional scope]: <description>\n\n[optional body]\n\n[optional footer(s)]\n```\n\nThe commit contains the following structural elements, to communicate intent to the consumers of your library:\n\n1. **fix:** a commit of the type `fix` patches gets released with a PATCH version bump\n1. **feat:** a commit of the type `feat` gets released as a MINOR version bump\n1. **BREAKING CHANGE:** a commit that has a footer `BREAKING CHANGE:` gets released as a MAJOR version bump\n1. types other than `fix:` and `feat:` are allowed and don't trigger a release\n\nIf a commit does not contain a conventional commit style message you can fix\nit during the squash and merge operation on the PR.\n\nOnce a commit has landed on the `main` branch a release will be created and automatically published to [pypi](https://pypi.org/)\nusing the GitHub Action in [.github/workflows/release.yaml](./.github/workflows/release.yaml) which uses [poetry](https://python-poetry.org/)\nto publish the package to pypi.\n\n## Copyright\n\nCopyright (c) 2022 [Radio Bern RaBe](http://www.rabe.ch)\n",
    'author': 'RaBe IT-Reaktion',
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
