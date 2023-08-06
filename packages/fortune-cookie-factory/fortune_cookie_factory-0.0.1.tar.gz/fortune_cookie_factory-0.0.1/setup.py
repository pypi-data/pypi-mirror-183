# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fortune_cookie']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['my-demo-script = fortune_cookie.app:open_cookie']}

setup_kwargs = {
    'name': 'fortune-cookie-factory',
    'version': '0.0.1',
    'description': '',
    'long_description': "name: learn-github-actions\nrun-name: ${{ github.actor }} is learning GitHub Actions\non: [push]\njobs:\n  check-bats-version:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v3\n      - uses: actions/setup-node@v3\n        with:\n          node-version: '14'\n      - run: npm install -g bats\n      - run: bats -v",
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
