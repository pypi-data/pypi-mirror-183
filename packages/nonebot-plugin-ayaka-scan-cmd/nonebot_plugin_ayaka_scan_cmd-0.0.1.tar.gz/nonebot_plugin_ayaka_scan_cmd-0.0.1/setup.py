# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

modules = \
['nonebot_plugin_ayaka_scan_cmd']
install_requires = \
['nonebot-plugin-ayaka>=1.0.0b0,<2.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ayaka-scan-cmd',
    'version': '0.0.1',
    'description': '扫描当前所有matcher，总结命令',
    'long_description': '<div align="center">\n\n# 命令探查 0.0.1\n\n</div>\n\n缓解下载了新插件却不会使用的焦虑\n\n使用`scan-all`指令，让bot展示一份简陋甚至错误百出的帮助菜单\n\n使用`scan-search <name>`指令，让bot展示`<name>`相关的内容\n\n使用`scan-list`指令，让bot展示所有模块名\n\n## 效果示例\n\n以安装了`nonebot_plugin_game_collection`为例\n\n`scan-search 赛马`\n\n```\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令] [cmds] \'创建赛马\'/\'赛马创建\'\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令] [cmds] \'开始赛马\'/\'赛马开始\'\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令] [cmds] \'暂停赛马\'/\'赛马暂停\'\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令] [cmds] \'赛马事件重载\'\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令] [cmds] \'赛马加入\'/\'加入赛马\'\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令] [cmds] \'赛马清空\'/\'清空赛马\'\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令] [cmds] \'赛马重置\'/\'重置赛马\'\n```\n\n## 实现原理\n\n遍历`nonebot.matcher.matchers`对象，分析所有`Matcher`\n',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bridgeL/nonebot-plugin-ayaka-scan-cmd',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
