# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zookeeper']

package_data = \
{'': ['*']}

install_requires = \
['nginxproxymanager>=0.1.0,<0.2.0', 'py-dactyl>=2.0.0,<3.0.0']

entry_points = \
{'console_scripts': ['stingray-zookeeper = zookeeper:__main__.main',
                     'zookeeper = zookeeper:__main__.main']}

setup_kwargs = {
    'name': 'stingray-zookeeper',
    'version': '0.1.0',
    'description': 'Zookeeper is a command-line utility for managing Stingray.',
    'long_description': '# zookeeper\n\n`stingray-zookeeper` on PyPI\n\nThis package lets you swiftly create & configure Stingray containers.\n\n## Installation & Use\n\n```bash\n# Install pipx to run stingray-zookeeper in a virtual environment\npip install pipx\n\n# Run this command for an explanation of the available arguments\npipx run stingray-zookeeper --help\n\n# Run stingray-zookeeper\n# Notes: your pterodactyl token will be longer than the example.\n#        nginxproxymanager tokens are long as shit because of their great amount of encoded json and large key\n#        these (obviously) aren\'t real keys.\n#        your nest, egg, and proxy ids will be different. \n#        check your pterodactyl settings & nginxproxymanager frontend.\npipx run stingray-zookeeper \\\n  --name "StingRay" \\\n  --nest 12 \\\n  --egg 45 \\\n  --proxy 43 \\\n  --panel-url "https://ptero.regulad.xyz" \\\n  --panel-key "ptla_wordswordswords" \\\n  --proxy-url "https://nginx.local.regulad.xyz" \\\n  --proxy-token "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkiLCJzY29wZSI6WyJ1c2VyIl0sImF0dHJzIjp7ImlkIjoxfSwiZXhwaXJlc0luIjoiMWQiLCJqdGkiOiJUdFlQaGhiRiIsImlhdCI6MTY3MjA5Mjk1NSwiZXhwIjoxNjcyMTc5MzU1fQ.rZFs0iT0PgvCOq5tWQd0dq-kP9GJ7_jbXnuwPS-GwHU"\n ```\n',
    'author': 'Parker Wahle',
    'author_email': 'parkeredwardwahle2017@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/regulad/zookeeper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
