# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['corpus_base', 'corpus_base.utils']

package_data = \
{'': ['*'], 'corpus_base': ['templates/*']}

install_requires = \
['citation-utils>=0.0.17,<0.0.18',
 'corpus-pax>=0.0.8,<0.0.9',
 'markdownify>=0.11.6,<0.12.0',
 'python-frontmatter>=1.0.0,<2.0.0',
 'unidecode>=1.3.6,<2.0.0']

setup_kwargs = {
    'name': 'corpus-base',
    'version': '0.0.12',
    'description': 'Initialize justice, decision, citation, voting, and opinion tables.',
    'long_description': '# Corpus-Base\n\nBuilds on top of *corpus-pax* to create additional tables related to the Supreme Court.\n\n```python shell\n>>> from corpus_base import build_sc_tables\n>>> build_sc_tables(c)\n```\n\nThis creates additional tables associated with:\n\n1. Justices\n2. Decisions\n   - Citations\n   - Votelines\n   - Titletags\n   - Opinions\n\n```python shell\n>>> from corpus_base import init_sc_cases\n>>> init_sc_cases(c, test_only=10)\n```\n\nParse through a locally downloaded repository to populate tables. Since there are thousands of cases, can limit the number of downloads via the `test_only` function attribute. The path location of the downloaded repository is [hard-coded](./corpus_base/utils/resources.py) since this package is intended to be run locally. Instructions for downloading and updating the repository are discussed elsewhere.\n\n## Full steps\n\n```python\nfrom corpus_pax import init_persons, init_person_tables\nfrom corpus_base import build_sc_tables, setup_case, init_sc_cases\nfrom sqlpyd import Connection\n\nc = Connection(DatabasePath="test.db")  # type: ignore\ninit_persons(c)  # for authors\nbuild_sc_tables(c)\ninit_sc_cases(c, test_only=10)\n```\n',
    'author': 'Marcelino G. Veloso III',
    'author_email': 'mars@veloso.one',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.11.0',
}


setup(**setup_kwargs)
