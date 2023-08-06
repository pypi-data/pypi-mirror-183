# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['encoder_interface']

package_data = \
{'': ['*']}

install_requires = \
['pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'encoder-interface1-0-0',
    'version': '1.0.0',
    'description': '',
    'long_description': '# Encoder-Interface\nPython package for interfacing with encoder systems.\n\n### Purpose of the Package\n+ Providing simple API functions for interfacing with the encoder.\n\n### Main API\n\n+ EncoderInterface: Main class for interfacing with the encoder.\n\n\n### Author\n+ Martin Porenta\n',
    'author': 'MartinP96',
    'author_email': 'porenta.martin@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
