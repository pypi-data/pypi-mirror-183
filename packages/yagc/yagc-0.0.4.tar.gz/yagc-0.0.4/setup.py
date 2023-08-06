# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yagc', 'yagc.git', 'yagc.github', 'yagc.tests.git', 'yagc.tests.github']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'gitpython>=3.1.29,<4.0.0',
 'pygithub>=1.57,<2.0',
 'semver==3.0.0-dev.4']

entry_points = \
{'console_scripts': ['yagc = yagc.cli:main']}

setup_kwargs = {
    'name': 'yagc',
    'version': '0.0.4',
    'description': 'Yet Another Git Convention(s) - rules for working with text together',
    'long_description': 'None',
    'author': 'Neon Law Foundation',
    'author_email': 'support@neonlaw.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
