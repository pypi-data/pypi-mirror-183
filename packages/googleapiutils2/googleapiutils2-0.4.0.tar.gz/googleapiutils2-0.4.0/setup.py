# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['googleapiutils2', 'googleapiutils2._types']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client-stubs>=1.11.0,<2.0.0',
 'google-api-python-client>=2.47.0,<3.0.0',
 'google-auth-httplib2>=0.1.0,<0.2.0',
 'google-auth-oauthlib>=0.5.1,<0.6.0',
 'pandas>=1.4.3,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'types-requests>=2.28.9,<3.0.0']

setup_kwargs = {
    'name': 'googleapiutils2',
    'version': '0.4.0',
    'description': '',
    'long_description': 'None',
    'author': 'Mike Babb',
    'author_email': 'mike7400@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
