# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jiav', 'jiav.api.backends', 'jiav.api.schemas']

package_data = \
{'': ['*']}

install_requires = \
['ansible-runner>=2.3.1,<3.0.0', 'ruamel-yaml>=0.17.21,<0.18.0']

setup_kwargs = {
    'name': 'jiav-backend-ansible',
    'version': '0.1.0',
    'description': 'Ansible backed for jiav tool',
    'long_description': '# jiav-backend-ansible\n\n## General\n\nAn Ansible backend for [jiav](https://github.com/vkhitrin/jiav).  \n**This package does not install Ansible itself; please ensure it is in your system/virtual environment.**\n\n**This backend is risky since it allows users to execute arbitrary commands, and use it at your own risk**.\n\n## Documentation\n\nVisit <https://jiav.readthedocs.io/en/latest/ansible_backend.html>.\n\n## Requirements\n\nInstall [jiav]([jiav](https://github.com/vkhitrin/jiav)).  \n`jiav` requires Python `>= 3.8`.\n\nAnsible installed.\n\n## Installation\n\nInstall from remote:\n\n```bash\npip3 install jiav-backend-ansible\n```\n\nInstall from the local repository:\n\n```bash\npip3 install .\n```\n\n## Contributing\n\n**All contributions are welcome!**\n',
    'author': 'Vadim Khitrin',
    'author_email': 'me@vkhitrin.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
