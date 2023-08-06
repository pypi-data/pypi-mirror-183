# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['findout', 'findout._utils', 'findout.domains']

package_data = \
{'': ['*']}

install_requires = \
['parsel>=1.6.0,<1.7.0', 'requests>=2.25.1,<2.26.0']

entry_points = \
{'console_scripts': ['findout = findout.findout:main']}

setup_kwargs = {
    'name': 'findout-in-comment',
    'version': '0.1.0',
    'description': 'A pre-attack hacker tool to find out sensitives comments in HTML',
    'long_description': '<h1 align="center">Find Out in Comment</h1>\n<h2 align="center" >\nFind sensetive comment out in HTML<br><br>\n    <a href="https://github.com/PabloEmidio/Findout-in-Comment/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/PabloEmidio/Findout-in-Comment?style=social"></a>\n    <a href="https://github.com/PabloEmidio"><img alt="GitHub followers" src="https://img.shields.io/github/followers/PabloEmidio?label=Follow%20me&style=social"></a>\n</h2>\n\n---\n\n# ⚈ About\nThis is a pre-attack hacker tool that searches for sensitives words in HTML comments tag and return some informations which can help in your attack process\n\n---\n\n# ⚈ Requirements\n\n```\npip3 install -r requirements.txt\n```\n---\n\n# ⚈ Use example\n\n<h3 align="center">Find default sensitives words out, showing entire tag comment and allowing to show comments with html code</h3>\n<p align="center">\n\n  <img align="center" src=".images/example_01.png"><br>\n</p>\n\n---\n\n<h3 align="center">Find default sensitives words out, showing entire tag comment, allowing to show comments with html code and taking the word "tag" out for the search</h3>\n\n<p align="center">\n  <img align="center" src=".images/example_02.png"><br>\n</p>\n\n---\n\n<h3 align="center">Find default sensitives words out in local file html, showing entire tag comment, allowing to show comments with html code and looking for optional word "md5"</h3>\n\n<p align="center">\n  <img align="center" src=".images/example_03.png"><br>\n</p>\n\n\n---\n\n\n# ⚈ Tech Stack\n\nThe following tools were used in the construction of the project:\n\n- [Python](https://www.python.org/)\n- [Parsel](https://pypi.org/project/parsel/)\n\n---\n\n# ⚈ Bugs and Features\n<p>\nPlease report any type of bug. Remember that this is an open source project and will evolve with everyone\'s help. :)<br>\nAny report will be read and will get due attention\n</p><br>\n<p>\nNew features are being done and new ideas are being created always that possible...<br>\nnew ideas will be accepted...\n</p>\n',
    'author': 'Pablo Emidio',
    'author_email': 'p.emidiodev@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/PabloEmidio/Findout-in-Comment',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
