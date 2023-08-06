# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['corpus_pax']

package_data = \
{'': ['*'], 'corpus_pax': ['templates/*']}

install_requires = \
['email-validator>=1.3.0,<2.0.0',
 'httpx>=0.23.0,<0.24.0',
 'jinja2>=3.1.2,<4.0.0',
 'sqlpyd>=0.1.1,<0.2.0']

setup_kwargs = {
    'name': 'corpus-pax',
    'version': '0.1.2',
    'description': 'Add content from Github to a local sqlite database, syncing images to Cloudflare, for later use.',
    'long_description': '# corpus-pax\n\nSetting up the initial, foundational tables with generic users and organizations.\n\n```mermaid\nflowchart LR\nrepo(((github/corpus))) --source of data---> local(local machine)\nlocal--run corpus-pax--->db[(sqlite.db)]\n```\n\nImplies the existence of an _updated_ Github `corpus` repository. Data concerning members will be pulled from such repository. Each avatar image should be named `avatar.jpeg` so that these can be uploaded to Cloudflare.\n\n## Install\n\n```zsh\npoetry add corpus-pax\npoetry update\n```\n\n## Supply .env\n\nCreate an .env file to create/populate the database. See [sample .env](.env.example) highlighting the following variables:\n\n1. Cloudflare `CF_ACCT`\n2. Cloudflare `CF_TOKEN`\n3. Github `EXPIRING_TOKEN`\n4. `DB_FILE` (sqlite)\n\nNote the [workflow](.github/workflows/main.yml) where the secrets are included for Github actions. Ensure these are set in the repository\'s `<url-to-repo>/settings/secrets/actions`, making the proper replacements when the tokens for Cloudflare and Github expire.\n\n### Notes\n\n#### Why Github\n\nThe names and profiles of individuals and organizations are stored in Github. These are pulled into the application via an API call requiring the use of a personal access token.\n\n#### Why Cloudflare Images\n\nIndividuals and organizations have images stored in Github. To persist and optimize images for the web, I use Cloudflare images.\n\n#### Why sqlite\n\nThe initial data is simple. This database however will be the foundation for a more complicated schema. Sqlite seems a better fit for experimentation and future embeddability of the same for app use.\n\n## Steps\n\n### Review database connection\n\nUse the database path declared in DB_FILE to establish an sqlite3 connection:\n\n```python\nfrom sqlpyd import Connection  # this is sqlite-utils\' Database() under the hood\n\nc = Connection()  # type: ignore\n\n# the filename will later be created in the root directory of the project folder\nConnection(DatabasePath="ex.db", WALMode=False)\n```\n\nThis connection will be used to access the database.\n\n## Add persons\n\nCreate and populate the _persons_-related tables:\n\n```python\nfrom corpus_pax import init_persons\n\n# This is a shortcut to: init_person_tables(c); add_individuals_from_api(c); and add_organization_from_api(c)\ninit_persons(c)\n```\n',
    'author': 'Marcelino G. Veloso III',
    'author_email': 'mars@veloso.one',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://lawdata.xyz',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.11.0',
}


setup(**setup_kwargs)
