# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dagster_meltano', 'dagster_meltano.log_processing']

package_data = \
{'': ['*']}

install_requires = \
['dagster>=1.0']

setup_kwargs = {
    'name': 'dagster-meltano',
    'version': '1.0.0',
    'description': 'A dagster plugin that allows you to run your Meltano project inside Dagster.',
    'long_description': 'None',
    'author': 'Jules Huisman',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
