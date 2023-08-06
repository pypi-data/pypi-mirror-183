# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['helloheart_airflow_utils', 'helloheart_airflow_utils.logging']

package_data = \
{'': ['*']}

install_requires = \
['apache-airflow<=1.10.15', 'markupsafe<=2.0.1', 'wtforms<=2.3.3']

setup_kwargs = {
    'name': 'helloheart-airflow-utils',
    'version': '0.2.3',
    'description': 'Apache Airflow Utilities',
    'long_description': '# HelloHeart Airflow Utilities\n\nUseful utilities for Apache Airflow, courtesy of HelloHeart.\n\nIt supports Python 3.6 - 3.8.\n\n## Installation\n\n### Install latest release\nLatest release are uploaded to PyPi, install using pip:\n\n```bash\npip install helloheart-airflow-utils\n```\n\n### Install from source to use latest development version\nInstall latest development version, clone the repository and install using Poetry:\n\n```bash\ngit clone https://github.com/Hello-Heart/helloheart-airflow-utils\ncd helloheart-airflow-utils\npoetry install\n```\n\n## Running the tests\n\n### Single Python version testing\nFor testing a single Python version, use pytest (after installing from source):\n\n```bash\npytest tests\n```\n\n### Multiple Python versions testing\nFor testing multiple Python versions, use tox:\n\n```bash\ntox\n```',
    'author': 'Ory Jonay',
    'author_email': 'ory.jonay@helloheart.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Hello-Heart/helloheart-airflow-utils',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<3.12',
}


setup(**setup_kwargs)
