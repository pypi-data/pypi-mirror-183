# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ayaka']

package_data = \
{'': ['*']}

install_requires = \
['nonebot-adapter-onebot>=2.1.3,<3.0.0', 'nonebot2>=2.0.0b5,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ayaka',
    'version': '1.0.0b0',
    'description': '为nonebot插件开发提供状态机支持',
    'long_description': '<div align="center">\n\n# Ayaka 1.0.0b0\n\n<img src="https://img.shields.io/pypi/pyversions/nonebot-plugin-ayaka">\n\n</div>\n\n## 文档\n\nhttps://bridgel.github.io/ayaka_doc/\n',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://bridgel.github.io/ayaka_doc/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
