# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['heatmapx']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.6.0,<3.0.0']

setup_kwargs = {
    'name': 'heatmapx',
    'version': '0.3.0',
    'description': 'Flexible, intuitive heatmap creation on NetworkX graphs',
    'long_description': '# HeatmapX: Heatmaps for NetworkX Graphs\n',
    'author': 'drmrd',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
