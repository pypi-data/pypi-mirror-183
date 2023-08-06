# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ayaka_games', 'ayaka_games.plugins', 'ayaka_games.plugins.data']

package_data = \
{'': ['*'], 'ayaka_games.plugins': ['data/calc_24/*', 'data/dragon/*']}

install_requires = \
['nonebot-plugin-ayaka>=1.0.0b1,<2.0.0', 'pypinyin>=0.47.1,<0.48.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ayaka-games',
    'version': '0.5.0',
    'description': 'ayaka小游戏合集',
    'long_description': '<div align="center">\n\n# ayaka文字小游戏合集 v0.5.0\n\n基于[ayaka](https://github.com/bridgeL/nonebot-plugin-ayaka)开发的文字小游戏合集\n\n开发进度 8/10，还剩2个小游戏等待构思\n\n**特别感谢**  [@灯夜](https://github.com/lunexnocty/Meiri) 大佬的插件蛮好玩的~\n\n</div>\n\n## 文档\n\nhttps://bridgel.github.io/ayaka_doc/latest/games/\n\n## 预告\n\n9号小游戏\n\n文字税\n\n只有买了文字的人才可以相互间收税\n\n管理员可以发起文字市场，此时市场公布一定数量的文字，所有人可以购买随机福袋抽取文字，同一文字可以多人持有，每个人的文字有效期都是24h\n\n文字市场持续10分钟\n\n24h内，若发言不小心包含了其他人的"版权文字"，则要支付使用费用，按字数收费\n\n每个文字的税都是固定的\n\n多人持有的文字，在收税时，其所得由多人平分\n',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bridgeL/nonebot-plugin-ayaka-games',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
