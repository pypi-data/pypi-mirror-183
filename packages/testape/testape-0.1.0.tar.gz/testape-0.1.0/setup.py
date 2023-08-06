# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['testape']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'testape',
    'version': '0.1.0',
    'description': 'SDK to create extsions for the Testape platform',
    'long_description': '# Testape SDK\n\n[![PyPI - Version](https://img.shields.io/pypi/v/testape.svg)](https://pypi.org/project/testape)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/testape.svg)](https://pypi.org/project/testape)\n\n---\n\n**Table of Contents**\n\n- [Installation](#installation)\n- [License](#license)\n\n## Installation\n\n```console\npip install testape\n```\n\nThen, in your code:\n\n```python\nfrom testape import TestapeClient\n\nclient = TestapeClient(api_key="<your_api_key>")\n\ndef func():\n    client.send_event()\n```\n\n## License\n\n`testape` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.\n',
    'author': 'Lior Pollak',
    'author_email': '4294489+liorp@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
