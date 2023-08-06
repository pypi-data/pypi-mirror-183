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
    'version': '0.0.2',
    'description': '扫描当前所有matcher，总结命令',
    'long_description': '<div align="center">\n\n# 命令探查 0.0.2\n\n</div>\n\n缓解下载了新插件却不会使用的焦虑\n\n使用`scan-all`指令，让bot展示一份简陋甚至错误百出的帮助菜单\n\n使用`scan-search <name>`指令，让bot展示`<name>`相关的内容\n\n使用`scan-list`指令，让bot展示所有模块名\n\n## 效果示例\n\n以安装了`nonebot_plugin_game_collection`为例\n\n`scan-search 赛马`\n\n```\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调位置] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令]\n  [cmds] \'创建赛马\'/\'赛马创建\'\n[回调注释] 无\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调位置] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令]\n  [cmds] \'加入赛马\'/\'赛马加入\'\n[回调注释] 无\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调位置] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令]\n  [cmds] \'清空赛马\'/\'赛马清空\'\n[回调注释] 无\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调位置] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令]\n  [cmds] \'赛马事件重载\'\n[回调注释] 无\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调位置] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令]\n  [cmds] \'赛马开始\'/\'开始赛马\'\n[回调注释] 无\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调位置] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令]\n  [cmds] \'赛马暂停\'/\'暂停赛马\'\n[回调注释] 无\n\nAyaka Bot(123) 说：\n[模块名称] nonebot_plugin_game_collection\n[回调位置] nonebot_plugin_game_collection\n[回调名称] _\n[可用命令]\n  [cmds] \'赛马重置\'/\'重置赛马\'\n[回调注释] 无\n```\n\n以安装了`nonebot_plugin_ayaka_games`为例\n\n`scan-search suspect`\n\n```\nAyaka Bot(123) 说：\n[模块名称] ayaka.box\n[回调位置] ayaka_games.plugins.who_is_suspect\n[回调名称] box_entrance\n[可用命令]\n  [cmds] \'谁是卧底\'\n  [other] 未知指令\n[回调注释] 打开应用\n\nAyaka Bot(123) 说：\n[模块名称] ayaka.box\n[回调位置] ayaka_games.plugins.who_is_suspect\n[回调名称] exit_play\n[可用命令]\n  [cmds] \'exit\'/\'退出\'\n  [other] 未知指令\n[回调注释] 无\n\nAyaka Bot(123) 说：\n[模块名称] ayaka.box\n[回调位置] ayaka_games.plugins.who_is_suspect\n[回调名称] exit_room\n[可用命令]\n  [cmds] \'exit\'/\'退出\'\n  [other] 未知指令\n[回调注释] 关闭游戏\n\nAyaka Bot(123) 说：\n[模块名称] ayaka.box\n[回调位置] ayaka_games.plugins.who_is_suspect\n[回调名称] join\n[可用命令]\n  [cmds] \'join\'/\'加入\'\n  [other] 未知指令\n[回调注释] 加入房间\n\nAyaka Bot(123) 说：\n[模块名称] ayaka.box\n[回调位置] ayaka_games.plugins.who_is_suspect\n[回调名称] leave\n[可用命令]\n  [cmds] \'离开\'/\'leave\'\n  [other] 未知指令\n[回调注释] 离开房间\n\nAyaka Bot(123) 说：\n[模块名称] ayaka.box\n[回调位置] ayaka_games.plugins.who_is_suspect\n[回调名称] play_info\n[可用命令]\n  [cmds] \'信息\'/\'info\'\n  [other] 未知指令\n[回调注释] 展示投票情况\n\nAyaka Bot(123) 说：\n[模块名称] ayaka.box\n[回调位置] ayaka_games.plugins.who_is_suspect\n[回调名称] room_info\n[可用命令]\n  [cmds] \'信息\'/\'info\'\n  [other] 未知指令\n[回调注释] 展示房间内成员列表\n\nAyaka Bot(123) 说：\n[模块名称] ayaka.box\n[回调位置] ayaka_games.plugins.who_is_suspect\n[回调名称] start\n[可用命令]\n  [cmds] \'start\'/\'begin\'/\'开始\'\n  [other] 未知指令\n[回调注释] 开始游戏\n\nAyaka Bot(123) 说：\n[模块名称] ayaka.box\n[回调位置] ayaka_games.plugins.who_is_suspect\n[回调名称] vote\n[可用命令]\n  [cmds] \'vote\'/\'投票\'\n  [other] 未知指令\n[回调注释] 请at你要投票的对象，一旦投票无法更改\n```\n\n\n## 实现原理\n\n遍历`nonebot.matcher.matchers`对象，分析所有`Matcher`\n',
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
