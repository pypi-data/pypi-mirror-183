# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_servicestate', 'nonebot_plugin_servicestate.protocol']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.20.0,<0.21.0',
 'nonebot-adapter-onebot>=2.1.0,<3.0.0',
 'nonebot2>=2.0.0b2,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-servicestate',
    'version': '0.0.3',
    'description': '基于NoneBot2的状态监测插件',
    'long_description': '<p align="center">\n  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>\n</p>\n\n<div align="center">\n\n# NoneBot Plugin ServiceStatus\n\n_✨ NoneBot 服务状态查询插件 ✨_\n\n</div>\n\n<p align="center">\n  <a href="https://raw.githubusercontent.com/nonebot/plugin-apscheduler/master/LICENSE">\n    <img src="https://img.shields.io/github/license/nonebot/plugin-apscheduler.svg" alt="license">\n  </a>\n  <a href="https://pypi.python.org/pypi/nonebot-plugin-apscheduler">\n    <img src="https://img.shields.io/pypi/v/nonebot-plugin-apscheduler.svg" alt="pypi">\n  </a>\n  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">\n</p>\n\n## 简介\n\n可通过 `服务状态` 查询当前服务器各功能 API 可用状态\n\n例如：\n\n```\nO 可用 | 会战面板\nO 可用 | SSH登录\nX 故障 | 涩图\nO 可用 | 画图\nX 故障 | ChatGPT\n```\n\n\n## 特色\n\n- 易于上手：所有配置项的增删查改都可通过文本交互实现，无需修改任何配置文件\n- 异步支持：所有协议均通过异步实现，无需担心探测过程中造成堵塞\n- 易于拓展：开发者只需继承内部抽象基类`BaseProtocol`并实现部分核心方法即可增添新协议支持\n\n\n## 安装\n\n使用 `nb-cli` 安装（推荐）：\n```\nnb plugin install nonebot-plugin-servicestate\n```\n\n使用 `git clone` 安装：\n```\ngit clone https://github.com/OREOCODEDEV/nonebot-plugin-servicestate.git\n```\n\n\n## 使用\n\n### 服务状态查询\n可通过发送 `服务状态` 获取当前绑定的监控服务可用状态\n\n### 新增监控服务\n可通过发送 `添加监控服务 <协议> <名称> <地址>` 以新增需要监控的服务\n```\n添加监控服务 HTTP git截图 https://github.com\n```\n\n### 修改监控服务\n可通过发送 `修改监控服务 <名称> <参数名> <参数内容>` 以修改监控服务的参数\n* 不同协议支持修改的参数内容不同，具体请参考下方协议篇\n```\n修改监控服务 git截图 proxy http://127.0.0.1:10809\n```\n\n### 群组监控服务\n**当前版本服务群组后暂不支持修改及解除群组，只能删除群组，请注意**\n\n当多个API共同支持某项服务时，可通过 `群组监控服务 <名称1> <名称2> <群组名称>` 群组多个服务为一个显示\n\n* 只有当群组中的所有服务都为可用状态时，群组才显示为可用，当有一个或多个服务为故障状态时，群组都显示为故障\n\n例：假设当前已设置好 涩图信息API 和 涩图图床 两个监控服务，可通过下列命令组合为一个服务\n```\n群组监控服务 涩图信息API 涩图图床 涩图\n```\n群组命令前：\n```\nO 可用 | 涩图信息API\nX 故障 | 涩图图床\n```\n群组命令后：\n```\nX 故障 | 涩图\n```\n\n### 群组监控服务\n可通过发送 `删除监控服务 <名称>` 以不再监测该服务\n```\n删除监控服务 git截图\n```\n\n\n## 协议支持\n\n以下是项目当前支持的协议，以及可被通过修改命令配置的字段\n\n### HTTP GET\n- [x] 状态查询：无关键字\n- [x] 监测地址：`host`\n- [x] 代理地址：`proxies`\n- [x] 超时时间：`timeout`\n- [ ] 请求头：暂未支持\n- [ ] UA：暂未支持\n- [ ] Cookie：暂未支持\n- [ ] 有效响应码：暂未支持\n\n### TCP\n- [x] 状态查询：无关键字\n- [x] 监测地址：`host`\n- [x] 端口：`port`\n- [ ] 代理地址：暂未支持\n- [ ] 超时时间：暂未支持\n\n### PING\n- [ ] 状态查询：暂未支持\n- [ ] 监测地址：暂未支持\n- [ ] 代理地址：暂未支持\n- [ ] 超时时间：暂未支持\n\n\n## Todo\n- [ ] 支持更多配置字段\n- [ ] 协议拓展接口增强\n- [ ] 解绑群组支持\n- [ ] 群组编辑支持\n',
    'author': 'OREOCODEDEV',
    'author_email': '17620745509@126.COM',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/OREOCODEDEV/nonebot-plugin-servicestate',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
