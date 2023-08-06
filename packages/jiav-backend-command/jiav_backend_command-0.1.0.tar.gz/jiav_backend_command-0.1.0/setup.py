# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jiav', 'jiav.api.backends', 'jiav.api.schemas']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'jiav-backend-command',
    'version': '0.1.0',
    'description': 'Command backend for jiav',
    'long_description': '# jiav-backend-command\n\n## General\n\nA command backend for [jiav](https://github.com/vkhitrin/jiav).  \n\n**This backend is risky since it allows users to execute arbitrary commands, and use it at your own risk**.\n\n## Documentation\n\nVisit <https://jiav.readthedocs.io/en/latest/ansible_backend.html>.\n\n## Requirements\n\nInstall [jiav]([jiav](https://github.com/vkhitrin/jiav)).  \n`jiav` requires Python `>= 3.8`.\n\n## Installation\n\nInstall from remote:\n\n```bash\npip3 install jiav-backend-command\n```\n\nInstall from the local repository:\n\n```bash\npip3 install .\n```\n\n## Contributing\n\n**All contributions are welcome!**\n',
    'author': 'Vadim Khitrin',
    'author_email': 'me@vkhitrin.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
