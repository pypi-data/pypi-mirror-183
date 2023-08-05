# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spoor']

package_data = \
{'': ['*']}

install_requires = \
['datadog>=0.44.0,<0.45.0', 'rich>=12.6.0,<13.0.0', 'varname>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'spoor',
    'version': '0.2.0',
    'description': 'Track functions invocations',
    'long_description': '## spoor\n\n```bash\n$ pip install spoor\n```\n\n### Configuration\n### TODO:\n\n* [ ] Add datadog exporter\n* [x] Add group methods by class option\n* [ ] Add tracking by import path\n* [x] Add `most_common` method for statistics\n',
    'author': 'Misha Behersky',
    'author_email': 'bmwant@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
