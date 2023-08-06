# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbttools']

package_data = \
{'': ['*']}

install_requires = \
['dbt-core>=1.3.1,<2.0.0',
 'gitpython>=3.1.29,<4.0.0',
 'invoke>=1.7.3,<2.0.0',
 'networkx>=2.8.8,<3.0.0',
 'pyvis>=0.3.1,<0.4.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['dbt-test = dbttools.main:program.run']}

setup_kwargs = {
    'name': 'dbt-tools',
    'version': '0.1.1',
    'description': 'Tools for dbt.',
    'long_description': 'None',
    'author': 'Indi Harrington',
    'author_email': 'hi@indigo.rocks',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
