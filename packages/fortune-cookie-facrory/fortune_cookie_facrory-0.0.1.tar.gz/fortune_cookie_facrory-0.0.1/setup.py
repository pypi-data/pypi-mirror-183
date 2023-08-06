# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fortune_cookie']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['my-demo-script = fortune_cookie.app:open_cookie']}

setup_kwargs = {
    'name': 'fortune-cookie-facrory',
    'version': '0.0.1',
    'description': '',
    'long_description': '',
    'author': 'yuyatinnefeld',
    'author_email': 'yuyatinnefeld@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
