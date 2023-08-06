# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['youdotcom']

package_data = \
{'': ['*']}

install_requires = \
['PyVirtualDisplay>=3.0,<4.0',
 'ascii-magic>=1.6,<2.0',
 'chromedriver-autoinstaller>=0.4.0,<0.5.0',
 'markdownify>=0.11.6,<0.12.0',
 'rich>=10.14.0,<11.0.0',
 'typer[all]>=0.4.0,<0.5.0',
 'undetected-chromedriver>=3.2.1,<4.0.0']

entry_points = \
{'console_scripts': ['youdotcom = youdotcom.__main__:app']}

setup_kwargs = {
    'name': 'youdotcom',
    'version': '0.2.1',
    'description': 'unofficial api wrapper for you.com and all of its apps',
    'long_description': '\n<h1 align="center">\n  <br>\n  <a href="https://github.com/SilkePilon/youdotcom/"><img src="https://github.com/SilkePilon/youdotcom/blob/main/youdotcom.png?raw=true" alt="Markdownify" width="200"></a>\n  <br>\n  YouDotCom for python\n  <br>\n</h1>\n\n<h4 align="center">An unofficial python library wrapper for <a href="http://you.com/" target="_blank">you.com</a> and all of its apps.</h4>\n\n<div align="center">\n\n  [![Python Version](https://img.shields.io/pypi/pyversions/youdotcom.svg)](https://pypi.org/project/youdotcom/)\n  [![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/silkepilon/youdotcom/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)\n\n  [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n  [![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)\n  [![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/silkepilon/youdotcom/blob/master/.pre-commit-config.yaml)\n  [![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/silkepilon/youdotcom/releases)\n  [![License](https://img.shields.io/github/license/silkepilon/youdotcom)](https://github.com/silkepilon/youdotcom/blob/master/LICENSE)\n  ![Coverage Report](assets/images/coverage.svg)\n  \n</div>\n\n<p align="center">\n  <a href="#key-features">Key Features</a> •\n  <a href="#how-to-use">How To Use</a> •\n  <a href="#install">Install</a> •\n  <a href="#credits">Credits</a> •\n  <a href="#license">License</a>\n</p>\n\n<!-- ![screenshot](https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/app/img/markdownify.gif) -->\n\n## Key Features\n* Bypass CloudFlare\n* Server ready\n  - Supports non-gui operating systems.\n* Cross platform\n  - Windows, macOS and Linux ready.\n\n## How To Use\n\nFirst you need to <a href="#install">Install</a> YouDotCom, then as example code for YouChat:\n\n```python\nfrom youdotcom.init import Init  # import the Init class\nfrom youdotcom.youchat import Chat  # import YouChat\n\ndriver = Init().driver  # setting up the webdriver. use `webdriver_path=` if the pre-installed one does not work.\n\n\nchat = Chat.send_message(driver=driver, message="what is the time?")  # send a message to YouChat. passing the driver and messages\n\ndriver.close()  # close the webdriver\n\n\nprint(chat)  # {\'message\': \'The current time is Saturday, December 31, 2022 09:47:30 UTC.\', \'time\': \'25\'}\n```\nor use:\n\n```youdotcom -example```\n\n> **Note**\n> YouDotCom is in Alpha and there will be bugs!\n\n\n## install\n\n```pip install youdotcom --upgrade```\n\n## Discord\n\nYouDotCom also has an official [discord server](https://discord.gg/SD7wZMFSvV), chat and help developers with there projects!\n\n## Credits\n\nThis software uses the following open source packages:\n\n- [undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)\n\n\n## License\n\nMIT\n\n---\n\n\n',
    'author': 'youdotcom',
    'author_email': 'silkepilon2009@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/silkepilon/youdotcom',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
