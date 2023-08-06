# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_oauth_hub',
 'django_oauth_hub.oauth_client',
 'django_oauth_hub.oauth_client.backend',
 'django_oauth_hub.oauth_client.migrations',
 'django_oauth_hub.oauth_client.models',
 'django_oauth_hub.oauth_server',
 'django_oauth_hub.oauth_server.migrations']

package_data = \
{'': ['*'], 'django_oauth_hub.oauth_client': ['templates/oauth_client/*']}

install_requires = \
['Authlib>=1.1.0,<2.0.0', 'django>=4.0,<5.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'django-oauth-hub',
    'version': '0.0.4',
    'description': 'OAuth client and server for Django using authlib.',
    'long_description': '# Django OAuth Hub\n\nOAuth client and server for Django using [Authlib](https://github.com/lepture/authlib).\n\n**NOTE: This library is still under development and mostly undocumented. It is currently not recommended for use in (production) applications.**\n\n## Features\n\nThis library consists of two modules: an OAuth client and an OAuth server. The two modules were designed to be used together, but they can also be used separately.\n\n### OAuth client\n- OAuth 1.0\n- OAuth 2.0\n- OpenID Connect (Discovery)\n- Configurable by database\n- Multiple clients per OAuth provider\n\n### OAuth server\n- OAuth 2.0\n- TODO\n\n## Documentation\nThe documentation is available [here](docs/index.md).\n\n## Contributing\nSee the [development documentation](docs/development.md). In the future more specific guidelines for contributing will be drafted. \n\n## License\nThis project is available under the [MIT license](LICENSE.md). Note that some dependencies have different licenses.\n',
    'author': 'Daniel Huisman',
    'author_email': 'daniel@huisman.me',
    'maintainer': 'Daniel Huisman',
    'maintainer_email': 'daniel@huisman.me',
    'url': 'https://github.com/DanielHuisman/django-oauth-hub',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
