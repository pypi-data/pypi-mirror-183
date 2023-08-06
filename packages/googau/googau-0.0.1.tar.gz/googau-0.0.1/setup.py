# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['googau', 'googau.constants']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=2.70.0,<3.0.0',
 'google-auth-httplib2>=0.1.0,<0.2.0',
 'google-auth-oauthlib>=0.8.0,<0.9.0']

setup_kwargs = {
    'name': 'googau',
    'version': '0.0.1',
    'description': 'A helper library for automating your work with Google Workspace',
    'long_description': '# Google Workspace Automation Toolbox\n\n## Installation\n\n1. Install from pypi\n\n   ```bash\n   pip install -U googau\n   ```\n\n1. Install for development\n\n   ```bash\n   virtualenv -p python3 venv\n   source venv/bin/activate\n   pip install poetry\n   poetry install\n   ```\n\n### References and links\n\nGoogle API documentation - [https://developers.google.com/](https://developers.google.com/)\n',
    'author': 'Theodore Aptekarev',
    'author_email': 'aptekarev+googau@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
