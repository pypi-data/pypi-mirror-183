# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_couplets']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0',
 'nonebot-adapter-onebot>=2.1,<3.0',
 'nonebot2>=2.0.0-rc.2,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-couplets',
    'version': '0.1.0',
    'description': 'Nonebot2对对联插件。',
    'long_description': '<div align="center">\n  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>\n  <br>\n  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>\n</div>\n\n<div align="center">\n\n# nonebot-plugin-couplets\n\n_✨ Nonebot2对对联插件 ✨_\n\n<a href="./LICENSE">\n    <img src="https://img.shields.io/github/license/CMHopeSunshine/nonebot-plugin-couplets.svg" alt="license">\n</a>\n<a href="https://pypi.python.org/pypi/nonebot-plugin-couplets">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-couplets.svg" alt="pypi">\n</a>\n<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n\n</div>\n\n## 📖 介绍\n\n基于[王斌给您对对联API](https://ai.binwang.me/couplet/)的Nonebot2对对联插件。\n\n## 💿 安装\n\n<details>\n<summary>使用 nb-cli 安装</summary>\n在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装\n\n    nb plugin install nonebot-plugin-couplets\n\n</details>\n\n<details>\n<summary>使用包管理器安装</summary>\n在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令\n\n<details>\n<summary>pip</summary>\n\n    pip install nonebot-plugin-couplets\n</details>\n<details>\n<summary>pdm</summary>\n\n    pdm add nonebot-plugin-couplets\n</details>\n<details>\n<summary>poetry</summary>\n\n    poetry add nonebot-plugin-couplets\n</details>\n<details>\n<summary>conda</summary>\n\n    conda install nonebot-plugin-couplets\n</details>\n\n打开 nonebot2 项目的 `bot.py` 文件, 在其中写入\n\n    nonebot.load_plugin(\'nonebot_plugin_couplets\')\n\n</details>\n\n\n## ☀ ️指令\n```\n对联 <上联内容> (数量)\n· 数量可选，默认为1\n```\n例如，`对联 苟利国家生死以 3`\n\n',
    'author': 'CMHopeSunshine',
    'author_email': '277073121@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/CMHopeSunshine/nonebot-plugin-couplets',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
