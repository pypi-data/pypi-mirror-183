# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['navercafe']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.2,<2.0.0',
 'pyperclip>=1.8.2,<2.0.0',
 'selenium>=4.7.2,<5.0.0',
 'webdriver-manager>=3.8.5,<4.0.0']

setup_kwargs = {
    'name': 'navercafe',
    'version': '0.1.0',
    'description': '',
    'long_description': "## Setup\n\n```\n$ pip install navercafe\n```\n\n## Usage\n\n```\nfrom navercafe import NaverCafe\n\ncafe = NaverCafe('wikibookstudy', '30853297')\ncafe.enter_id_pw('your_id', 'your_pw')  # Need manual authentication\n\ndf = cafe.articleboard(34)\nprint(len(df))\nprint(df.head())\n```\n",
    'author': 'Yong Choi',
    'author_email': 'sk8er.choi@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
