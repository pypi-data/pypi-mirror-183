# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_release_test', 'poetry_release_test.test', 'poetry_release_test.tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'poetry-release-test',
    'version': '0.0.0',
    'description': 'test release through poetry',
    'long_description': '\n# poetry应用\n[github](https://github.com/python-poetry/poetry)\n\n[官方文档](https://link.zhihu.com/?target=https%3A//python-poetry.org/docs/)\n## 安装\n`pip install poetry`\n\n## tips\n`poetry new`创建一个项目脚手架，包括基本结构、pyproject.toml文件，基于每个人的项目目录不同，推荐在已有项目添加poetry管理,详见./test\n\n`poetry init`在现有项目里创建**pyproject.toml**文件\n\n`poetry config --list`查看config列表\n\n`poetry config virtualenvs.in-project true`配置在项目内创建.venv\n\n`poetry config <key> <value>`\n\n`poetry env use python3`指定创建虚拟环境时使用的python解释器版本\n\n### 运行环境指定\n- 执行poetry的命令并不需要激活虚拟环境，因为poetry会自动检测当前虚拟环境\n- 在当前目录对应虚拟环境中执行命令`poetry run python test.py`\n- 显示激活的虚拟环境`poetry shell`\n\n### 依赖\n> 安装某个包时，会在pyproject.toml文件中默认使用版本限定，比如colorama = "^0.4.1" ，当我执行 poetry update 时，colorama也许会更新到0.4.9，但绝不会更新到0.5.0，意思是在更新依赖时不会修改最左边非零的数字号版本，这样的默认设定可以确保不会更新到不兼容变动的版本。\n\n`poetry add flask`安装最新稳定版本的flask\n\n`poetry add pytest --dev`指定为开发依赖，会写到pyproject.toml中的[[tool.poetry.dev-dependencies]]区域\n\n`poetry add flask=2.22.0`指定具体的版本\n\n`poetry install`安装pyproject.toml文件中的全部依赖\n\n`poetry install --no-dev`只安装非development环境的依赖，一般部署时使用\n\n`poetry show`查看项目安装的依赖\n\n`poetry show -t`树形结构查看项目安装的依赖\n\n`poetry update`更新所有锁定版本的依赖\n\n`poetry update httprunner`更新指定的依赖\n\n`poetry remove packages`卸载依赖, **会将依赖包一起卸载**\n\n`poetry env list --full-path`查找当前项目的虚拟环境\n\n\n### 发布流程\n\n1. 原项目中同级目录\n\n\n## 配置镜像源\n- 豆瓣 http://pypi.doubanio.com/simple/\n- 网易 http://mirrors.163.com/pypi/simple/\n- 阿里云 http://mirrors.aliyun.com/pypi/simple/\n- 清华大学 http://pypi.tuna.tsinghua.edu.cn/simple/\n\n在`pyproject.toml`文件末尾追加以下内容\n```\n[[tool.poetry.source]]\nname = "aliyun"\nurl = "http://mirrors.aliyun.com/pypi/simple"\ndefault = true\n```',
    'author': 'songhaoyanga',
    'author_email': '1627635056@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
