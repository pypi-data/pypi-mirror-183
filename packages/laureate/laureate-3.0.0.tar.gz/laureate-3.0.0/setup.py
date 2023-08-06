# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['laureate']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'requests>=2.28.1,<3.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['laureate = laureate.laureate:cli']}

setup_kwargs = {
    'name': 'laureate',
    'version': '3.0.0',
    'description': 'Generate Homebrew formulae for Poetry projects',
    'long_description': '# laureate has been deprecated\n\nlaureate has been succeeded by [poetry-brew](https://github.com/celsiusnarhwal/poetry-brew).\n\n```bash\npoetry self add poetry-brew\n```\n',
    'author': 'celsius narhwal',
    'author_email': 'hello@celsiusnarhwal.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/celsiusnarhwal/laureate',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
