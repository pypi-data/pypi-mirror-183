# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dim']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'dim-python',
    'version': '0.1.0',
    'description': 'Python implementation of dim (Data Installation Manager): Manage open data in your projects, like a package manager.',
    'long_description': "# dim-python\n\n`dim-python` is a Python implementation of [dim (Data Installation Manager): Manage open data in your projects, like a package manager](https://github.com/c-3lab/dim).\n\n## Join community\n\nWe are looking for members to develop together as an open source community.\n\n[Slack](https://join.slack.com/t/c3lab-hq/shared_invite/zt-v6zz66n9-1VYkVXC4zoQViWSMdzMTLg)\n\n## Quick Start\n\n1. Install the dim\n\nhttps://github.com/c-3lab/dim#install-the-dim\n\n2. Install the python-dim\n\n```\n$ pip install python-dim\n```\n\n3. Initialize the project for dim\n\n```\n$ dim init\n```\n\nAlso can initialize the project using dim-python.\n\n4. Use the python-dim\n\n```python\nimport dim\n\ndim.install('https://example.com/xxx.json', 'example_name', ['encode utf-8'])\n\nprint(dim.list())\n\n```\n\n\n## Build\n\nInstall Python 3.8+.\n\nThen, install `poetry` 1.2.0+ as follows.\n\nWindows:\n\n```Bash\n# Linux, macOS, Windows (WSL)\ncurl -sSL https://install.python-poetry.org | python3 -\n# Windows (Powershell)\n(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -\n```\n\nInstall dependencies with `poetry`.\n\n```Bash\npoetry install\n```\n\n### Check version of dim\n\n```Python\nimport dim\ndim.__version__\n```\n\n## License\n\nRefer to [MIT License](https://github.com/c-3lab/dim-python/blob/main/LICENSE).\n",
    'author': 'C3Lab',
    'author_email': 'info.c3lab@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/c-3lab/dim-python/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
