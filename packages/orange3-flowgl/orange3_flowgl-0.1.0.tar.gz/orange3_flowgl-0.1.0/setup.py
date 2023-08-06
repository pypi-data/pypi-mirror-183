# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['orangecontrib', 'orangecontrib.flowgl', 'orangecontrib.flowgl.widgets']

package_data = \
{'': ['*'], 'orangecontrib.flowgl.widgets': ['icons/*']}

install_requires = \
['AnyQt>=0.2.0,<0.3.0', 'flowgl>=0.1.2,<0.2.0', 'pandas>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'orange3-flowgl',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Orange3 Flow Immersive\n\nThis is the Orange3 add-on for pushing data to Flow.\n\n## Installation\n\n### Production\n\nOpen Orange3, navigate to `Options -> Add-ons...`, select `Add more...`, type in `orange3-flowgl`, and press `Add`. \n\n### Development\n\nIn the same python environment as Orange3 is installed, run:\n\n```bash\npip install -e .\n```\n',
    'author': 'Flow Immersive',
    'author_email': 'info@flow.gl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
