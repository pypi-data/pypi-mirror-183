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
    'version': '0.1.1',
    'description': 'A pre-attack hacker tool to find out sensitives comments in HTML',
    'long_description': '<h1 align="center">Find Out in Comment</h1>\n<h2 align="center" >\nFind sensetive comment out in HTML<br><br>\n    <a href="https://github.com/PabloEmidio/Findout-in-Comment/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/PabloEmidio/Findout-in-Comment?style=social"></a>\n    <a href="https://github.com/PabloEmidio"><img alt="GitHub followers" src="https://img.shields.io/github/followers/PabloEmidio?label=Follow%20me&style=social"></a>\n</h2>\n\n---\n\n# ⚈ About\nThis is a pre-attack hacker tool that searches for sensitives words in HTML comments tag and return some informations which can help in your attack process\n\n---\n\n# ⚈ How to use\n\n```bash\n$ pip install findout-in-comment\n$ findout -v --return-tags $URL_OR_FILE_PATH\n```\n\n---\n\n\n# ⚈ Tech Stack\n\nThe following tools were used in the construction of the project:\n\n- [Python](https://www.python.org/)\n- [Parsel](https://pypi.org/project/parsel/)\n- [Poetry](https://python-poetry.org/)\n- [Flake8](https://flake8.pycqa.org/en/latest/)\n- [pre-commit](https://pre-commit.com/)\n---\n\n# ⚈ Bugs and Features\n<p>\nPlease report any type of bug. Remember that this is an open source project and will evolve with everyone\'s help. :)<br>\nAny report will be read and will get due attention\n</p><br>\n<p>\nNew features are being done and new ideas are being created always that possible...<br>\nnew ideas will be accepted...\n</p>\n',
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
