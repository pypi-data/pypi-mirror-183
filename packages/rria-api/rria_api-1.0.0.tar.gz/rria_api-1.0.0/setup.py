# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rria_api', 'rria_api.gen3', 'rria_api.gen3.api_gen3', 'rria_api.ned']

package_data = \
{'': ['*']}

install_requires = \
['pyniryo>=1.1.2,<2.0.0']

setup_kwargs = {
    'name': 'rria-api',
    'version': '1.0.0',
    'description': '',
    'long_description': '# robot-api\n Robot API\n\nLinks Úteis:\nhttps://docs.niryo.com/dev/ros/v4.1.1/en/source/overview.html',
    'author': 'felipeadsm',
    'author_email': '97059009+felipeadsm@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
