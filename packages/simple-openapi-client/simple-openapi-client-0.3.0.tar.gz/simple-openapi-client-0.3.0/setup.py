# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_openapi_client', 'simple_openapi_client.openapi']

package_data = \
{'': ['*'], 'simple_openapi_client': ['templates/*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0', 'black>=22.6.0,<23.0.0', 'httpx>=0.23.0,<0.24.0']

setup_kwargs = {
    'name': 'simple-openapi-client',
    'version': '0.3.0',
    'description': 'OpenAPI Python client generator that follows the KISS principle.',
    'long_description': "# Simple Open API Client generator\n\nThis project was made to generate a simple client (async or not) from an openapi\nspecifications (unlike other client generators, which typically produce\ncode that is difficult for python beginners to use). It aims to produce a\nsingle file that contains the Client class.\n\n## Notes\nThis project is in alpha and has probably bugs.\nIssues/bugfixes/additions are welcome.\n\n## Installation\n```shell\n$ pip install simple-openapi-client\n```\n\n## Usage\n\nThis package is usage from a Python script.\nSimply load the openapi file (from local file or url) and make the client.\n\nFor instance:\n\n```py\nfrom simple_openapi_client import parse_openapi, make_client, Config\n\nconfig = Config(client_name='Orthanc', package_name='client')\ndocument = parse_openapi(url_or_path='https://api.orthanc-server.com/orthanc-openapi.json')\nclient_str = make_client(document, config, use_black=True)\n\nwith open(f'./{config.package_name}.py', 'w') as file:\n    file.write(client_str)\n```\n\nOr, for an async client:\n\n```py\nfrom simple_openapi_client import parse_openapi, make_client, Config\n\nconfig = Config(client_name='AsyncOrthanc', package_name='async_client')\ndocument = parse_openapi(url_or_path='https://api.orthanc-server.com/orthanc-openapi.json')\nclient_str = make_client(document, config, async_mode=True, use_black=True)\n\nwith open(f'./{config.package_name}.py', 'w') as file:\n    file.write(client_str)\n```\n",
    'author': 'Gabriel Couture',
    'author_email': 'gacou54@gmail.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gacou54/openapi-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
