# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['requests_decorator']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.3,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'requests-decorator',
    'version': '0.1.0',
    'description': 'Python HTTP for (lazy) humans.',
    'long_description': None,
    'author': 'conor-od',
    'author_email': 'codonnell872@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
