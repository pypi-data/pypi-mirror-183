# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['insomnia']

package_data = \
{'': ['*']}

install_requires = \
['humanize>=4.4.0,<5.0.0',
 'psutil>=5.9.4,<6.0.0',
 'rich>=13.0.0,<14.0.0',
 'textual>=0.9.0,<0.10.0']

entry_points = \
{'console_scripts': ['insomnia = insomnia.tui:main',
                     'insomniascript = insomnia.insomnia:main']}

setup_kwargs = {
    'name': 'insomnia-app',
    'version': '0.1.0',
    'description': 'A TUI app to find out why your computer stays awake at night',
    'long_description': '# insomnia\nA TUI app to find out why your computer stays awake at night.\n',
    'author': 'David Fokkema',
    'author_email': 'davidfokkema@icloud.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/davidfokkema/insomnia',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
