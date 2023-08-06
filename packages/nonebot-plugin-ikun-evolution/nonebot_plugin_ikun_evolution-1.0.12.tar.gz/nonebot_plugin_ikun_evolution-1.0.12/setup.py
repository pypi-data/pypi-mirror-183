# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_ikun_evolution',
 'nonebot_plugin_ikun_evolution.model',
 'nonebot_plugin_ikun_evolution.psql_db',
 'nonebot_plugin_ikun_evolution.service',
 'nonebot_plugin_ikun_evolution.xiaor_battle_system',
 'nonebot_plugin_ikun_evolution.xiaor_battle_system.src',
 'nonebot_plugin_ikun_evolution.xiaor_battle_system.src.tools']

package_data = \
{'': ['*'],
 'nonebot_plugin_ikun_evolution': ['gamedata/*',
                                   'gamedata/image/item/*',
                                   'gamedata/image/notice/*',
                                   'gamedata/json/*',
                                   'gamedata/notice/*']}

install_requires = \
['gino>=1.0.1,<2.0.0',
 'json5>=0.9.10,<0.10.0',
 'lagom>=2.2.0,<3.0.0',
 'nonebot-adapter-onebot>=2.0.0-beta.1,<3.0.0',
 'nonebot2>=2.0.0-beta.1,<3.0.0',
 'python-dateutil>=2.7']

setup_kwargs = {
    'name': 'nonebot-plugin-ikun-evolution',
    'version': '1.0.12',
    'description': '移植自真寻的q群小游戏',
    'long_description': "# 只因进化录\n\n移植自真寻的[只因进化录](https://github.com/RShock/ikun_evolution)\n\n## 安装\n\n### 前置条件\n\n* python版本应当大于3.9\n* gocqhttp为rc3以上，否则可能存在组消息发送为空的情况\n* 没有使用`SQLAlchemy1.4`的插件，如[GenshinUID](https://github.com/KimigaiiWuyi/GenshinUID)。以及其他使用数据库的插件也可能导致问题。\n如果存在，运行时会出现以下错误\n```\nmodule 'sqlalchemy.sql.schema' has no attribute '_schema_getter'\n```\n并且`poetry install`无法成功。\n具体可以在`poetry.lock`文件里搜索`sqlalchemy`观看是否有插件在使用1.4版本。\n这个问题影响范围很大。根本冲突是真寻在使用sqlalchemy1.3（gino）但是nonebot普遍使用1.4，导致我只能选一边，没有解决方案。仅剩方案是同时开多个bot。\n\n### 插件安装\n```\npip install nonebot_plugin_ikun_evolution\n```\n在 nonebot2 项目中设置 load_plugin()\n```\nnonebot.load_plugin('nonebot_plugin_ikun_evolution')\n```\n\n或者直接下载拖到插件文件夹里。\n\n### 数据库配置\n\n你需要安装一个[postgresql数据库](https://hibikier.github.io/zhenxun_bot/docs/installation_doc/install_postgresql.html)才能进行游戏\n\n安装完毕后，在`env.dev`里填上刚刚的数据库链接\n```\npsql = postgresql://名字:密码@127.0.0.1:5432/数据库名字\n```\n\n如果按真寻教程就是\n```\npsql = postgresql://uname:zhenxun@127.0.0.1:5432/testdb\n```\n\n这步有点困难，好处是再也不用担心误删数据库了。请加油罢\n\n## 已知问题\n\n在初次运行时，无法正确加载资源。\n\n只需要再运行一次bot，看见\n```\nnonebot_plugin_ikun_evolution | 【只因进化录】资源载入中\nnonebot_plugin_ikun_evolution | 【只因进化录】任务载入完成，共9个任务\nnonebot_plugin_ikun_evolution | 【只因进化录】制作表载入完成，共1个配方\nnonebot_plugin_ikun_evolution | 【只因进化录】地图载入完成，共42张地图\nnonebot_plugin_ikun_evolution | 【只因进化录】帮助载入完成，共11条帮助\nnonebot_plugin_ikun_evolution | 【只因进化录】技能载入完成，共38个技能\nnonebot_plugin_ikun_evolution | 【只因进化录】敌人载入完成，共30个敌人\nnonebot_plugin_ikun_evolution | 【只因进化录】物品载入完成，共7个物品\n```\n即为载入完成\n",
    'author': '小r',
    'author_email': '418648118@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/RShock/nonebot_plugin_ikun_evolution',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
