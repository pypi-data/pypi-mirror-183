# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['evcnet']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.21.0,<0.22.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'evcnet',
    'version': '0.1.1a3',
    'description': '',
    'long_description': "# python-evcnet\nPython client to retrieve data from evc-net.com\n\n\n```python\nfrom evcnet import Evcnet\ne = Evcnet(\n    url='https://evcompany.evc-net.com',\n    username='username@example.com',\n    password='s3cret'\n)\ne.login()\ne.total_usage()\n{'totalUsage': 5659, 'totalProvided': 4217}\n```\n",
    'author': 'Henk Kraal',
    'author_email': 'hkraal@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
