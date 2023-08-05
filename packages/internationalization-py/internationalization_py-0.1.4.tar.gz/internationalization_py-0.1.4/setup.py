# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['internationalization',
 'internationalization.loaders',
 'internationalization.types']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8', 'pyyaml>=5.0']

setup_kwargs = {
    'name': 'internationalization-py',
    'version': '0.1.4',
    'description': 'Internationalization library for comfortable usage',
    'long_description': '# Internationalization.py\nProvides simple and powerful i18n realization\n\n## Installation\n\n#### With pip\n```shell\npip install internationalization.py\n```\n#### Via Git\n```shell\ngit clone https://github.com/cortelf/internationalization.py\ncd internationalization.py\npython setup.py install\n```\n\n## Usage\n#### Create directory for yaml files\n```shell\nmkdir yourdirectory\n```\n#### Write your yaml files\nYou can use .yml or .yaml file extensions\n```shell\nen.yml\n```\n```yaml\nhello_world: Hello World!\n```\n```shell\nit.yml\n```\n```yaml\nhello_world: Ciao mondo!\n```\n#### In root of your app initialize singleton\n```python\nfrom internationalization import Internationalization\nfrom internationalization.loaders import YAMLLoader\n\ni18n = Internationalization()\ni18n.initialize(YAMLLoader("yourdirectory"))\n```\n#### It\'s ready to use in any place\n```python\nfrom internationalization import Internationalization\n\ni18n = Internationalization()\nenglish = i18n.get_language("en")\nitalian = i18n.get_language("it")\n\nprint("English:", english.hello_world)\nprint("Italian:", italian.hello_world)\n```',
    'author': 'CortelF',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/cortelf/internationalization.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
