# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['target_elasticsearch']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'elasticsearch>=8.5.2,<9.0.0',
 'jsonpath-ng>=1.5.3,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'singer-sdk>=0.9.0,<0.10.0',
 'time-machine>=2.8.2,<3.0.0',
 'types-python-dateutil>=2.8.19,<3.0.0']

entry_points = \
{'console_scripts': ['target-elasticsearch = '
                     'target_elasticsearch.target:TargetElasticsearch.cli']}

setup_kwargs = {
    'name': 'target-elasticsearch',
    'version': '1.0.0',
    'description': '`target-elasticsearch` is a singer target using the meltano SDK for targets',
    'long_description': None,
    'author': 'DT Mirizzi',
    'author_email': 'dtmirizzi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
