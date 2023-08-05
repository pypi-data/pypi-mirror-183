# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyprql',
 'pyprql.cli',
 'pyprql.magic',
 'pyprql.pandas_accessor',
 'pyprql.tests']

package_data = \
{'': ['*'], 'pyprql': ['assets/*']}

install_requires = \
['Pygments>=2.11.2,<3.0.0',
 'SQLAlchemy>=1.4.32,<2.0.0',
 'click>=8.0.4,<9.0.0',
 'duckdb-engine>=0.6.5,<0.7.0',
 'fuzzyfinder>=2.1.0,<3.0.0',
 'icecream>=2.1.2,<3.0.0',
 'ipython>=8.0,<9.0',
 'jupysql>=0.5.1,<0.6.0',
 'jupyter>=1.0.0,<2.0.0',
 'numpy>=1.22.3,<2.0.0',
 'pandas>=1.4,<2.0',
 'prompt-toolkit>=3.0.28,<4.0.0',
 'prql-python>=0.3,<0.4',
 'pytest>=7.1.2,<8.0.0',
 'rich>=12.0.0,<13.0.0',
 'traitlets>=5.2.0,<6.0.0']

entry_points = \
{'console_scripts': ['pyprql = pyprql.cli.__init__:main']}

setup_kwargs = {
    'name': 'pyprql',
    'version': '0.5.11',
    'description': 'Python extensions for PRQL',
    'long_description': "# pyprql\n\n[![CI/CD](https://github.com/prql/pyprql/actions/workflows/pull-request.yaml/badge.svg?branch=main)](https://github.com/prql/pyprql/actions/workflows/pull-request.yaml)\n[![Documentation Status](https://readthedocs.org/projects/pyprql/badge/?version=latest)](https://pyprql.readthedocs.io/en/latest/?badge=latest)\n\n![PyPI](https://img.shields.io/pypi/v/pyprql)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyprql)\n[![Codestyle: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n<!-- [![codecov](https://codecov.io/gh/prql/PyPrql/branch/main/graph/badge.svg?token=C6J2UI7FR5)](https://codecov.io/gh/prql/PyPrql) -->\n\npyprql contains:\n\n- pyprql.pandas_accessor — Pandas integration for PRQL\n- pyprql.magic — IPython magic for connecting to databases using `%%prql`\n\nFor docs, Check out the [pyprql docs](https://pyprql.readthedocs.io/), and the\n[PRQL Book][prql_docs].\n\n## Installation\n\n```bash\npip install pyprql\n```\n\n## Usage\n\n### Pandas integration\n\n```python\nimport pandas as pd\nimport pyprql.pandas_accessor\n\ndf = (...)\nresults_df = df.prql.query('select [age,name,occupation] | filter age > 21')\n```\n\n### Jupyter Magic\n\n```python\nIn [1]: %load_ext pyprql.magic\nIn [2]: %prql postgresql://user:password@localhost:5432/database\nIn [3]: %%prql\n   ...: from p\n   ...: group categoryID (\n   ...:   aggregate [average unitPrice]\n   ...: )\nIn [4]: %%prql results <<\n   ...: from p\n   ...: aggregate [min unitsInStock, max unitsInStock]\n\n```\n\n## Support\n\nThis project was created by\n[@charlie-sanders](https://github.com/charlie-sanders/) &\n[@rbpatt2019](https://github.com/rbpatt2019) and is now maintained by the\nbroader prql team.\n\n[prql_docs]: https://prql-lang.org/book\n",
    'author': 'Charlie Sanders',
    'author_email': 'charlie.fats@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://prql-lang.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
