# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lark2ldap']

package_data = \
{'': ['*']}

install_requires = \
['django>=3.2,<5.0']

setup_kwargs = {
    'name': 'lark2ldap',
    'version': '0.1.0',
    'description': 'Django app,to sync feishu contacts to ldap.',
    'long_description': "# Poetry Template\n\nDjango app template, using `poetry-python` as dependency manager.\n\nThis project is a template that can be cloned and re-used for\nredistributable apps.\n\nIt includes the following:\n\n* `poetry` for dependency management\n* `isort`, `black`, `pyupgrade` and `flake8` linting\n* `pre-commit` to run linting\n* `mypy` for type checking\n* `tox` and Github Actions for builds and CI\n\nThere are default config files for the linting and mypy.\n\n## Principles\n\nThe motivation for this project is to provide a consistent set of\nstandards across all YunoJuno public Python/Django projects. The\nprinciples we want to encourage are:\n\n* Simple for developers to get up-and-running\n* Consistent style (`black`, `isort`, `flake8`)\n* Future-proof (`pyupgrade`)\n* Full type hinting (`mypy`)\n\n## Versioning\n\nWe currently support Python 3.7+, and Django 3.2+. We will aggressively\nupgrade Django versions, and we won't introduce hacks to support\nbreaking changes - if Django 4 introduces something that 2.2 doesn't\nsupport we'll drop it.\n\n## Tests\n\n#### Tests package\n\nThe package tests themselves are _outside_ of the main library code, in\na package that is itself a Django app (it contains `models`, `settings`,\nand any other artifacts required to run the tests (e.g. `urls`).) Where\nappropriate, this test app may be runnable as a Django project - so that\ndevelopers can spin up the test app and see what admin screens look\nlike, test migrations, etc.\n\n#### Running tests\n\nThe tests themselves use `pytest` as the test runner. If you have\ninstalled the `poetry` evironment, you can run them thus:\n\n```\n$ poetry run pytest\n```\n\nor\n\n```\n$ poetry shell\n(my_app) $ pytest\n```\n\nThe full suite is controlled by `tox`, which contains a set of\nenvironments that will format, lint, and test against all\nsupport Python + Django version combinations.\n\n```\n$ tox\n...\n______________________ summary __________________________\n  fmt: commands succeeded\n  lint: commands succeeded\n  mypy: commands succeeded\n  py37-django22: commands succeeded\n  py37-django32: commands succeeded\n  py37-djangomain: commands succeeded\n  py38-django22: commands succeeded\n  py38-django32: commands succeeded\n  py38-djangomain: commands succeeded\n  py39-django22: commands succeeded\n  py39-django32: commands succeeded\n  py39-djangomain: commands succeeded\n```\n\n#### CI\n\nThere is a `.github/workflows/tox.yml` file that can be used as a\nbaseline to run all of the tests on Github. This file runs the oldest\n(2.2), newest (3.2), and head of the main Django branch.\n",
    'author': 'Huangxinyu',
    'author_email': 'huangxinyu.2991@gmail.com',
    'maintainer': 'Huangxinyu',
    'maintainer_email': 'huangxinyu.2991@gmail.com',
    'url': 'https://github.com/huangxy29/lark_to_ldap',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
