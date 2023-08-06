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
    'version': '1.1.2',
    'description': "Automated entry of job application data into Connecticut's DOL ReEmployCT portal.",
    'long_description': '# Connecticut Dep. of Labor ReEmployCT Automated Data Entry\n[![Python application](https://github.com/ariffjeff/ReEmployCT-Data-Entry/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/ariffjeff/ReEmployCT-Data-Entry/actions/workflows/python-app.yml)\n[![Upload Python Package](https://github.com/ariffjeff/ReEmployCT-Data-Entry/actions/workflows/python-publish.yml/badge.svg?branch=main)](https://github.com/ariffjeff/ReEmployCT-Data-Entry/actions/workflows/python-publish.yml)\n\nA Python CLI that automates entry of unemployment benefits data (weekly work search and certification) into Connecticut\'s DOL [ReEmployCT portal](https://reemployct.dol.ct.gov). ([More information on ReEmployCT](https://portal.ct.gov/dol/Unemployment-Benefits))\n\nWeekly job application data from an Excel file that the user actively maintains is accessed and automatically entered into ReEmployCT through a web browser instance controlled by Selenium. The program automates as much of the process as possible, such as login, data entry, page navigation, and secure user [credential handling](#user-credentials). The user will only need to interact for data entry review/confirmation and for captchas that need to be solved. Once the user finishes any required interaction then the program automatically takes back control. The program will walk you through setting everything up to get you on your way (see [Setup](#setup-python) first).\n\n## Requirements\n- Firefox\n- Excel\n- User job application data must only include U.S. addresses (ReEmployCT requirement)\n- Minimum of 3 work searches (job applications) per week (ReEmployCT requirement)\n- Currently only job applications are supported by this program as data entries into ReEmployCT from the Excel file. (Job applications are defined as "employer contacts" by CT DOL). In other words, a valid work search such as a job fair attendance can not be entered by this program and instead would need to be entered into ReEmployCT manually.\n\n## How to use\n### Install ([PyPI](https://pypi.org/project/reemployct-data-entry/))\n`pip install reemployct-data-entry`\n\n\n\n### Setup (Python)\nYou first need to get your copy of the Excel file that the program knows how to read job application data from:\n```\nfrom reemployct_data_entry import entry\n```\nThis will import the module you\'ll use to run the program, but also provide you with the path to the provided Excel template. Make a copy of `workSearch_template.xlsx`, save it wherever (and rename it whatever) you want. Open your copy, remove the row that contains the example job application, and start adding your own data (in the same format as the example row).\n\nTip: You can use `CTRL` + `;` on a cell in Excel to enter the current date. The format is MM/DD/YYYY which is what the program expects.\n\n\n### Run\nYou can either run from the CLI with:\n```\nentry.main()\n```\nOr simply click `entry.py` to run it.\n\n## User Credentials\nTo make the entire process streamlined, you can save your ReEmployCT login credentials when prompted by the CLI. Your credentials are encrypted and stored locally in the project folder in `credFile.ini` (only the username is left as plaintext). The encryption key is stored in `key.key`. You also have the option when saving your credentials to set an expiry time so that you will need to save a new set of credentials on a certain date.\n\n### Resetting saved credentials\n1. Delete `credFile.ini` from the project folder\n2. You will be prompted for new credentials when you run `entry.main()`\n',
    'author': 'Ariff Jeff',
    'author_email': 'ariffjeff@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ariffjeff/ReEmployCT-Data-Entry',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
