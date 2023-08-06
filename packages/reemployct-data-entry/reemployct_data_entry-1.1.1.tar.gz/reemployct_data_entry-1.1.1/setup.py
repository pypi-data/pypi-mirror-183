# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reemployct_data_entry', 'reemployct_data_entry.lib']

package_data = \
{'': ['*']}

install_requires = \
['colorama', 'cryptography', 'openpyxl', 'pandas', 'selenium', 'usaddress']

setup_kwargs = {
    'name': 'reemployct-data-entry',
    'version': '1.1.1',
    'description': "Automated entry of weekly job search and certification data into Connecticut's DOL ReEmployCT portal.",
    'long_description': "# DOLWeeklyClaimDataEntry\n Automated entry of weekly certification data into Connecticut's DOL ReEmployCT portal.\n",
    'author': 'Ariff',
    'author_email': 'ariffjeff@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
