# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_revoke']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.2.0,<3.0.0', 'nonebot2>=2.0.0rc2,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-revoke',
    'version': '0.1.0',
    'description': '',
    'long_description': '<!-- markdownlint-disable MD033 MD036 MD041 -->\n\n<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\nnonebot-plugin-revoke\n============\n\n_✨ 让机器人撤回自己发出的消息 ✨_\n\n</div>\n\n<p align="center">\n  <a href="https://raw.githubusercontent.com/ssttkkl/nonebot-plugin-revoke/master/LICENSE">\n    <img src="https://img.shields.io/github/license/ssttkkl/nonebot-plugin-revoke.svg" alt="license">\n  </a>\n  <a href="https://pypi.python.org/pypi/nonebot-plugin-revoke">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-revoke.svg" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.9+-blue.svg" alt="python">\n</p>\n\n\n## 使用方法\n\n对某条消息**回复**`/revoke`或`/撤回`\n\n（注意：仅超级用户可用）\n',
    'author': 'ssttkkl',
    'author_email': 'huang.wen.long@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
