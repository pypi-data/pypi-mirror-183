# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bany',
 'bany.cmd',
 'bany.cmd.extract',
 'bany.cmd.extract.extractors',
 'bany.core',
 'bany.ynab']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'diskcache>=5.4.0,<6.0.0',
 'oauthlib>=3.2.2,<4.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pdfplumber>=0.7.6,<0.8.0',
 'py-moneyed>=3.0,<4.0',
 'pydantic>=1.10.4,<2.0.0',
 'pytest>=7.2.0,<8.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'requests>=2.28.1,<3.0.0',
 'responses>=0.22.0,<0.23.0',
 'rich>=13.0.0,<14.0.0']

entry_points = \
{'console_scripts': ['bany = bany.__main__:main']}

setup_kwargs = {
    'name': 'bany',
    'version': '1.0.0',
    'description': '',
    'long_description': "# BANY\n\nA collection of scripts I've created to aid with budgeting using YNAB\n\n# Setup\n\n```bash\npipx install bany\n```\n\n## Create YNAB transactions from a PDF\n\n### `cfgs/extract-pdf-sample.yaml`\n\n- Define rules to match patterns in the text of a PDF\n- Define the transactions to create from these matches\n\n```yaml\n# Regular Expressions defined for date like values\ndates:\n  Force Date:\n    value: |-\n      2023-01-01\n\n  Check Date:\n    regex: |-\n      Check\\s+Date\\s+(?P<DATE>{MONTHS}\\s+\\d+,?\\s+\\d\\d\\d\\d)\n\n# Regular Expressions defined for money like values\namounts:\n  401K:\n    group: EARNINGS\n    inflow: true\n    regex: |-\n      401K\\s+\n      (?P<HOURS>{NUMBER})\\s+\n      (?P<MONEY>{AMOUNT})\\s+\n      (?P<TOTAL>{AMOUNT})\n\n  Salary:\n    group: EARNINGS\n    inflow: true\n    regex: |-\n      REGULAR\\s+\n      (?P<RATES>{NUMBER})\\s+\n      (?P<HOURS>{NUMBER})\\s+\n      (?P<MONEY>{AMOUNT})\\s+\n      (?P<TOTAL>{AMOUNT})\n\n  TOTAL-EARNINGS:\n    group: EARNINGS\n    inflow: true\n    total: true\n    regex: |-\n      Gross\\s+Earnings\\s+\n      (?P<HOURS>{NUMBER})\\s+\n      (?P<MONEY>{AMOUNT})\\s+\n      (?P<TOTAL>{AMOUNT})\n\n# Transactions to push to a YNAB budget (these may reference the matches defined above)\ntransactions:\n- budget: 2023\n  account: 'Checking'\n  category: 'Internal Master Category: Inflow: Ready to Assign'\n  payee: Company\n  color: red\n  amount: Salary\n  date: Check Date\n\n- budget: 2023\n  account: 'Company'\n  category: 'Investment: Fidelity'\n  payee: 'Transfer : Fidelity : Syapse'\n  memo: 2023\n  color: yellow\n  amount: 401K\n  date: Check Date\n\n```\n\n### `bany extract pdf`\n\n- Run the extact command to parse a PDF and upload transactions to YNAB\n\n```bash\nbany extract pdf --inp /path/to/pdf --config config.yaml\nbany extract pdf --inp /path/to/pdf --config config.yaml --upload\n```\n",
    'author': 'Adam Gagorik',
    'author_email': 'adam.gagorik@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
