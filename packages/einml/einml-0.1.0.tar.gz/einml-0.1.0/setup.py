# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['einml']

package_data = \
{'': ['*']}

install_requires = \
['datasets>=2.8,<3.0',
 'einops>=0.6,<0.7',
 'enlighten>=1.11,<2.0',
 'icecream>=2.1,<3.0',
 'keras-nlp>=0.4,<0.5',
 'matplotlib>=3.6,<4.0',
 'numpy>=1.24,<2.0',
 'nvsmi>=0.4,<0.5',
 'plotly>=5.11,<6.0',
 'python-box>=6.1,<7.0',
 'randomname>=0.1,<0.2',
 'tensorflow-probability>=0.19,<0.20',
 'tensorflow>=2.11,<3.0',
 'tf-models-official>=2.11,<3.0',
 'wandb>=0.13,<0.14']

setup_kwargs = {
    'name': 'einml',
    'version': '0.1.0',
    'description': 'Tensorflow utility library',
    'long_description': '# EinML Tensorflow\n\nThis helper library includes:\n- Utility functions\n- Re-exports for Einops\n- Tensorflow type annotations\n- A progress bar for training.\n',
    'author': 'Max Clarke',
    'author_email': 'maxeonyx@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
