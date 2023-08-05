# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_epicfree']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.20.0,<1.0.0',
 'nonebot-adapter-onebot>=2.0.0b1',
 'nonebot-plugin-apscheduler>=0.1.0',
 'nonebot2>=2.0.0b3',
 'pytz']

setup_kwargs = {
    'name': 'nonebot-plugin-epicfree',
    'version': '0.2.5',
    'description': 'EpicGameStore free games promotions plugin for NoneBot2',
    'long_description': '<h1 align="center">NoneBot Plugin EpicFree</h1></br>\n\n\n<p align="center">🤖 用于获取 Epic 限免游戏资讯的 NoneBot2 插件</p></br>\n\n\n<p align="center">\n  <a href="https://github.com/monsterxcn/nonebot_plugin_epicfree/actions">\n    <img src="https://img.shields.io/github/actions/workflow/status/monsterxcn/nonebot_plugin_epicfree/publish.yml?branch=main&style=flat-square" alt="actions">\n  </a>\n  <a href="https://raw.githubusercontent.com/monsterxcn/nonebot_plugin_epicfree/master/LICENSE">\n    <img src="https://img.shields.io/github/license/monsterxcn/nonebot_plugin_epicfree?style=flat-square" alt="license">\n  </a>\n  <a href="https://pypi.python.org/pypi/nonebot_plugin_epicfree">\n    <img src="https://img.shields.io/pypi/v/nonebot_plugin_epicfree?style=flat-square" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.8+-blue?style=flat-square" alt="python"><br />\n</p></br>\n\n\n**安装方法**\n\n\n使用以下命令之一快速安装（若配置了 PyPI 镜像，你可能无法及时检索到插件最新版本）：\n\n\n``` zsh\nnb plugin install nonebot_plugin_epicfree\n\npip install --upgrade nonebot_plugin_epicfree\n```\n\n\n重启 Bot 即可体验此插件。\n\n\n<details><summary><i>关于 NoneBot2 及相关依赖版本</i></summary></br>\n\n\n在已淘汰的 NoneBot2 适配器 [nonebot-adapter-cqhttp](https://pypi.org/project/nonebot-adapter-cqhttp/) 下，切记不要使用 `pip` 或 `nb_cli` 安装此插件。通过拷贝文件夹 `nonebot_plugin_epicfree` 至 NoneBot2 插件目录、手动安装 `nonebot-plugin-apscheduler` 和 `httpx` 依赖的方式仍可正常启用此插件。在未来某个版本会完全移除该适配器支持，请尽快升级至 [nonebot-adapter-onebot](https://pypi.org/project/nonebot-adapter-onebot/)。\n\n\n</details>\n\n\n<details><summary><i>关于 go-cqhttp 版本</i></summary></br>\n\n\n插件发送消息依赖 [@Mrs4s/go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 的合并转发接口，如需启用私聊响应请务必安装 [v1.0.0-rc2](https://github.com/Mrs4s/go-cqhttp/releases/tag/v1.0.0-rc2) 以上版本的 go-cqhttp。\n\n\n</details>\n\n\n**使用方法**\n\n\n```python\n# nonebot_plugin_epicfree/__init__.py#L27\nepic_matcher = on_regex(r"^(epic)?喜(加|\\+|＋)(一|1)$", priority=2, flags=IGNORECASE)\n\n# nonebot_plugin_epicfree/__init__.py#L39\nsub_matcher = on_regex(r"^喜(加|\\+|＋)(一|1)(私聊)?订阅(删除|取消)?$", priority=1)\n```\n\n\n - 发送「喜加一」查找限免游戏\n - 发送「喜加一订阅」订阅游戏资讯\n - 发送「喜加一订阅删除」取消订阅游戏资讯\n\n\n*\\* 插件响应基于正则匹配，所以，甚至「EpIc喜+1」这样的指令都可用！*\n\n\n**环境变量**\n\n\n```\nRESOURCES_DIR="/data/bot/resources"\nEPIC_SCHEDULER="8 8 8"\n```\n\n\n限免游戏资讯订阅功能默认在机器人根目录下 `/data/epicfree` 文件夹内生成配置文件。定义 `RESOURCES_DIR` 环境变量即可指定用于存放订阅配置的文件夹，填写包含 `epicfree` 文件夹的 **父级文件夹** 路径即可。如果是 Windows 系统应写成类似 `D:/path/to/resources_dir` 的格式。\n\n限免游戏资讯订阅默认 08:08:08 发送（如果当天的游戏已经推送过则不产生推送），定义 `EPIC_SCHEDULER` 环境变量即可指定推送时间，该配置的三个数字依次代表 `hour` `minute` `second`。\n\n\n**特别鸣谢**\n\n\n[@nonebot/nonebot2](https://github.com/nonebot/nonebot2/) | [@Mrs4s/go-cqhttp](https://github.com/Mrs4s/go-cqhttp) | [@DIYgod/RSSHub](https://github.com/DIYgod/RSSHub) | [@SD4RK/epicstore_api](https://github.com/SD4RK/epicstore_api)\n\n\n> 作者是 NoneBot2 新手，代码写的较为粗糙，欢迎提出修改意见或加入此插件开发！溜了溜了...\n',
    'author': 'monsterxcn',
    'author_email': 'monsterxcn@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/monsterxcn/nonebot_plugin_epicfree',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
