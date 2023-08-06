# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['driver']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.2,<0.24.0', 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['driver = driver.command:app']}

setup_kwargs = {
    'name': 'driver-downloader',
    'version': '0.2.0',
    'description': 'chromedriver downloader',
    'long_description': '### 这是一个使用npmmirror 中国镜像站的chromedriver 同步工具\n\n用于同步chromedriver的最新版本到本地\n\n使用\n* 安装\n\n      pip install driver-downloader\n\n* 命令行 使用\n\n      driver --help\n\n* python 使用\n    ```python\n    from driver import downloader\n    downloader()\n    ```\n',
    'author': 'Tai',
    'author_email': 'flywacool@gmail.com',
    'maintainer': 'Tai Hui',
    'maintainer_email': 'flywacool@gmail.com',
    'url': 'https://github.com/modaye/driver',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
