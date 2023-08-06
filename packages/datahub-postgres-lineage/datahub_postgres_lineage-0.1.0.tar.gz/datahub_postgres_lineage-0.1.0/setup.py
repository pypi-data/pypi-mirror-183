# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datahub_postgres_lineage']

package_data = \
{'': ['*']}

install_requires = \
['acryl-datahub[sqlalchemy]>=0.9.3.2,<0.10.0.0',
 'geoalchemy2>=0.12.5,<0.13.0',
 'psycopg2-binary>=2.9.5,<3.0.0',
 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'datahub-postgres-lineage',
    'version': '0.1.0',
    'description': 'Extract table lineage from Postgres views',
    'long_description': 'None',
    'author': 'Contiamo',
    'author_email': 'developers@contiamo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<3.11',
}


setup(**setup_kwargs)
