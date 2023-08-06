# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['zipndel']

package_data = \
{'': ['*']}

install_requires = \
['jupyterlab>=3.5.2,<4.0.0', 'numpy>=1.24.1,<2.0.0', 'pandas==1.5.2']

setup_kwargs = {
    'name': 'zipndel',
    'version': '0.1.0',
    'description': 'Zipndel is a lightweight python package equipped with two main functionalities; Zipndel or Unzipndel The Zipndel class provides automatic functionality for zipping or unzipping a password-protected pandas DataFrame file, and then deleting the original file.',
    'long_description': None,
    'author': 'QDaria',
    'author_email': 'mo@qdaria.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
