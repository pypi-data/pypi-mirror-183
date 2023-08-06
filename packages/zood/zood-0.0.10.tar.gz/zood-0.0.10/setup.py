# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zood', 'zood.MarkdownParser']

package_data = \
{'': ['*'], 'zood': ['config/*']}

install_requires = \
['PyYAML>=6.0,<7.0']

entry_points = \
{'console_scripts': ['zood = zood.main:main']}

setup_kwargs = {
    'name': 'zood',
    'version': '0.0.10',
    'description': 'web page documentation & comment generation documentation',
    'long_description': '# zood\n\nGithub仓库网页文档 + 注释生成文档\n\n## [主题预览](https://luzhixing12345.github.io/zood/)\n\n## 快速开始\n\n### 1.安装\n\n```bash\npip install zood\n```\n\n### 2.运行\n\n进入当前项目根目录\n\n- 根据markdown文档生成网页\n\n  ```bash\n  zood -g ./docs\n  ```\n\n  > `docs` 为markdown文档文件夹名\n\n- 根据代码注释生成网页文档\n\n  ```bash\n  zood -c\n  ```\n\n### 3.查阅[配置文档](https://luzhixing12345.github.io/zood/)\n\n```bash\nzood -h\n```\n\n## 开发\n\n```bash\npoetry build\n```\n\n```bash\npoetry config pypi-token.pypi my-token\n```\n\n```bash\npoetry publish\n```\n',
    'author': 'kamilu',
    'author_email': 'luzhixing12345@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/luzhixing12345/zood',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
