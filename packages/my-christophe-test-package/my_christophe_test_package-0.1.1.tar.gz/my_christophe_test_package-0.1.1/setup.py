# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['my_christophe_test_package']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'my-christophe-test-package',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Test package\n\nFoo.\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/DataDog/guarddog',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
