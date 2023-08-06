# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['dynamicprompts', 'dynamicprompts.generators', 'dynamicprompts.parser']

package_data = \
{'': ['*']}

install_requires = \
['pyparsing>=3.0.9,<4.0.0', 'requests>=2.28.1,<3.0.0', 'tqdm>=4.64.1,<5.0.0']

extras_require = \
{'attentiongrabber': ['spacy[attentiongrabber]>=3.4.4,<4.0.0']}

setup_kwargs = {
    'name': 'dynamicprompts',
    'version': '0.1.2',
    'description': 'Dynamic prompts templating library for Stable Diffusion',
    'long_description': '',
    'author': 'Adi Eyal',
    'author_email': 'adi@clearforest.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
