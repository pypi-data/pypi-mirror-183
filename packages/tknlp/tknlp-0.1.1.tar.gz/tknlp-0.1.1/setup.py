# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tknlp']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.5,<2.0.0']

setup_kwargs = {
    'name': 'tknlp',
    'version': '0.1.1',
    'description': '',
    'long_description': '# TKNLP\n\n\nRun NLP tools in an easier manner\n\n## Installation\n\n```bash\npip install tknlp\n```\n',
    'author': 'dennislblog',
    'author_email': 'dennisl@udel.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
