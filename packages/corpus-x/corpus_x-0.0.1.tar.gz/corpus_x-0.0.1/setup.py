# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['corpus_x', 'corpus_x.utils']

package_data = \
{'': ['*'],
 'corpus_x': ['sql/analysis/*',
              'sql/base/*',
              'sql/codes/*',
              'sql/codes/events/*',
              'sql/decisions/*',
              'sql/decisions/inclusions/*',
              'sql/statutes/*',
              'sql/statutes/references/*']}

install_requires = \
['corpus-base>=0.1.0,<0.2.0', 'statute-trees>=0.0.18,<0.0.19']

setup_kwargs = {
    'name': 'corpus-x',
    'version': '0.0.1',
    'description': 'Add codification and statute tables to pre-existing corpus-base database.',
    'long_description': '# corpus-x\n\n## Concept\n\n[corpus-pax](https://github.com/justmars/corpus-pax) + [corpus-base](https://github.com/justmars/corpus-base) + [statute-trees](https://github.com/justmars/statute-trees) = converts raw `yaml`-based corpus repository to its database variant **corpus-x**; see [details](notebooks/setup.ipynb). After constructing all of the required tables, it becomes possible to [evaluate the raw data](docs/5-db-evaluate.md).\n\n## Flow\n\n### Local files\n\nDownload *.yaml files from repository:\n\n```mermaid\nflowchart LR\nrepo(((github/corpus))) --download---> local(local machine)\n```\n\n### Local database\n\nSetup local db:\n\n```mermaid\nflowchart LR\n  local(local corpus)--add corpus-pax tables--->db\n  local--add corpus-base tables-->db\n  local--format trees with statute-trees-->trees\n  trees(tree structures)--add corpus-x tables-->db[(sqlite.db)]\n```\n\n### Replicated database\n\nStore backup db on aws:\n\n```mermaid\nflowchart LR\n\n  db[(sqlite.db)]--litestream replicate-->aws\n  aws--litestream restore-->lawdata.xyz\n```\n\n## Mode\n\nOrder | Time | Instruction | Docs\n:--:|:--:|--:|:--\n0 | ~6sec (if with test data) | [corpus-pax](https://github.com/justmars/corpus-pax#read-me) pre-requiste before `corpus-base` can work. |[Setup](docs/1-setup.md)\n1 | ~20-40min | [corpus-base](https://github.com/justmars/corpus-base#read-me) pre-requiste before `corpus-x` can work. |[Setup](docs/1-setup.md)\n2 | ~120-130min | If inclusion files not yet created, run script to generate. |[Pre-inclusions](docs/2-pre-inclusions.md)\n3 | ~10min | Assuming inclusion files are already created, can populate the various tables under `corpus-x` | [Post-inclusions](docs/3-post-inclusions.md)\n4 | ~60min | Litestream output `x.db` on AWS bucket | [Replicated db](docs/4-aws-replicate.md)\n\n## Gotchas\n\nThe statutory event data contained in the `units` field does not yet contain the `statute_id`s. Note that, prior to database insertion, we only know the statute label but not the id. Once the statute has been inserted, we can now match the statute label to the id:\n\n```python\nfor row in c.db[CodeRow.__tablename__].rows:\n    obj = CodeRow.set_update_units(c, row["id"])\n```\n',
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
