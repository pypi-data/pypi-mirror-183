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
    'version': '0.2.0',
    'description': '',
    'long_description': "## Setup\n\n```\n$ pip install navercafe\n```\n\n## Usage\n\n```\nfrom navercafe import NaverCafe\n\n# 1. setup\ncafe_name = 'wikibookstudy'\nclub_id = '30853297'\ncafe = NaverCafe(cafe_name, club_id)\n\n# 2. (optional) enter user id and pw\n# This is semi-automatic (needs manual authentication)\ncafe.enter_id_pw('your_id', 'your_pw')\n\n# 3. get article board\nboard_id = 34\ndf1 = cafe.articleboard(board_id)\nprint(len(df1))\nprint(df1.head())\n\n# 4. get comments\narticle_id = 139\ndf2 = cafe.comments(article_id)\nprint(len(df2))\nprint(df2.head())\n```\n\n",
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
