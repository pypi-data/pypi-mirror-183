# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mpl_mollier_axes', 'mpl_mollier_axes.axes']

package_data = \
{'': ['*']}

install_requires = \
['PsychroLib>=2.5.0,<3.0.0', 'matplotlib>=3.6.2,<4.0.0']

extras_require = \
{'CoolProp': ['CoolProp>=6.4.3,<7.0.0']}

setup_kwargs = {
    'name': 'mpl-mollier-axes',
    'version': '0.1.0',
    'description': "Matplotlib Axes class providing the transform for plotting 'Mollier-style' psychrometric charts.",
    'long_description': None,
    'author': 'woistdiekatze',
    'author_email': 'woistdiekatze.4x61i@simplelogin.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
