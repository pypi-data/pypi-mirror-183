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
    'version': '0.1.2',
    'description': 'Extract table lineage from Postgres views',
    'long_description': "# Datahub Postgres View Lineage\n\n\nA ingestion source to generate lineage for views in a Postgres database.\n\n\n## Quick Start\n\nFirst install [Poetry](https://python-poetry.org/docs/#installation) and [task](https://taskfile.dev) and initialize the project\n\n```sh\ntask setup\n```\n\nNow, start a database\n\n```sh\ntask start wait sample-view\n```\n\nNow run the ingestion to the console\n```sh\ntask run\n```\n\nWhen it is successful, the output should include\n\n```sh\nSource (datahub_postgres_lineage.ingestion.PostgresLineageSource) report:\n{'events_produced': '1',\n 'events_produced_per_sec': '26',\n 'event_ids': ['urn:li:dataset:(urn:li:dataPlatform:postgres,cool_db.public.emails,PROD)-upstreamLineage'],\n 'warnings': {},\n 'failures': {},\n 'filtered': ['public.names'],\n 'start_time': '2022-12-20 16:09:46.105046 (now).',\n 'running_time': '0.04 seconds'}\n```\n\n## Configuration\n\n| Key | Description | Default |\n| --- | --- | --- |\n| `username` | The username to connect to the database | '' |\n| `password` | The password to connect to the database | '' |\n| `host_port` | The host and port to connect to the database | '' |\n| `database` | The database to connect to | '' |\n| `database_alias` | Alias to apply to database when ingesting. | '' |\n| `sqlalchemy_uri` | SQLAlchemy URI to connect to the database | '' |\n| `scheme` | The SQLAlchemy scheme to use | `postgressql+psycopg2` |\n| `schema_pattern` | | |\n| `schema_pattern.allow`| Regexp pattern to match schemas to include | `.*` |\n| `schema_pattern.deny` | Regexp pattern to match schemas to exclude, 'information_schema' and 'pg_catalog' are already excluded | '' |\n| `view_pattern` | | |\n| `view_pattern.allow` | Regexp pattern to match view names to include | `.*` |\n| `view_pattern.deny` | Regexp pattern to match view names to exclude | '' |",
    'author': 'Contiamo',
    'author_email': 'developers@contiamo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/contiamo/datahub-postgres-lineage',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<3.11',
}


setup(**setup_kwargs)
