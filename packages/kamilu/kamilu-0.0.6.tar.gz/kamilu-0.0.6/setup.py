# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kamilu']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['kamilu = kamilu.main:main']}

setup_kwargs = {
    'name': 'kamilu',
    'version': '0.0.6',
    'description': 'computer graphics animation engine',
    'long_description': '# kamilu\n\n计算机绘图，动画引擎\n\n## 安装\n\n```bash\npip install kamilu\n```',
    'author': 'luzhixing12345',
    'author_email': 'luzhixing12345@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/luzhixing12345/kamilu',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
