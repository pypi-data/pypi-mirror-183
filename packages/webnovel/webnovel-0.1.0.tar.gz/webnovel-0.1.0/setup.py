# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webnovel']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'webnovel',
    'version': '0.1.0',
    'description': '',
    'long_description': '\n-  react + ant-design 构建原型\n- 抓取管理原型\n- 阅读原型\n- 抓取api\n- 阅读api\n\n',
    'author': 'Meng Xiangzhuo',
    'author_email': 'aumo@foxmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
