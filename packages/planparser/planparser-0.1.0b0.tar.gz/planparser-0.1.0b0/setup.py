# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['planparser', 'tests']

package_data = \
{'': ['*'], 'tests': ['test_data/*', 'test_data/floorplans/*']}

install_requires = \
['click', 'pytesseract>=0.3.10,<0.4.0']

entry_points = \
{'console_scripts': ['planparser = planparser.cli:cli']}

setup_kwargs = {
    'name': 'planparser',
    'version': '0.1.0b0',
    'description': 'Top-level package for planparser.',
    'long_description': '==========\nplanparser\n==========\n\n\n.. image:: https://img.shields.io/pypi/v/planparser.svg\n        :target: https://pypi.python.org/pypi/planparser\n\n.. image:: https://img.shields.io/travis/briggySmalls/planparser.svg\n        :target: https://travis-ci.com/briggySmalls/planparser\n\n.. image:: https://readthedocs.org/projects/planparser/badge/?version=latest\n        :target: https://planparser.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n\n\n\nTool for reading floorplan images\n\n\n* Free software: MIT\n* Documentation: https://planparser.readthedocs.io.\n\n\nFeatures\n--------\n\n* TODO\n\nCredits\n-------\n\nThis package was created with Cookiecutter_ and the `briggySmalls/cookiecutter-pypackage`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`briggySmalls/cookiecutter-pypackage`: https://github.com/briggySmalls/cookiecutter-pypackage\n',
    'author': 'Sam Briggs',
    'author_email': 'planparser@sambriggs.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/briggySmalls/planparser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)
