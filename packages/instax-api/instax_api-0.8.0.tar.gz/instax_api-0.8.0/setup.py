# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['instax', 'instax.tests']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.3.0,<10.0.0', 'loguru>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'instax-api',
    'version': '0.8.0',
    'description': 'A Python module and app to print photos on the Fujifim Instax Printers',
    'long_description': "# instax_api\n[![.github/workflows/python-test.yml](https://github.com/jpwsutton/instax_api/actions/workflows/python-test.yml/badge.svg)](https://github.com/jpwsutton/instax_api/actions/workflows/python-test.yml)\n[![Coverage Status](https://img.shields.io/coveralls/jpwsutton/instax_api/master.svg)](https://coveralls.io/github/jpwsutton/instax_api?branch=master)\n\nThis is a Python Module to interact and print photos to the Fujifilm Instax SP-2 and SP-3 printers.\n\n\n## Install this library\n\nIn order to use this library, you will need to be using Python 3\n\n```\npip3 install instax-api\n```\n\n\n## Usage\n\n**note** - From version 0.7.0 to 0.8.0, I moved away from adding a script to just calling the module from pyton using the `-m` argument.\n\n```\n$ python3 -m instax.print --help\nusage: instax-print [-h] [-i PIN] [-v {1,2,3}] image\n\npositional arguments:\n  image                 The location of the image to print.\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -i PIN, --pin PIN     The pin code to use, default: 1111.\n  -v {1,2,3}, --version {1,2,3}\n                        The version of Instax Printer to use (1, 2 or 3).\n                        Default is 2 (SP-2).                       \n```\n\n### Examples:\n\n - Printing a Photo to an SP-2 printer: `python3 -m instax.print myPhoto.jpg`\n - Printing a Photo to an SP-3 printer: `python3 -m instax.print myPhoto.jpg -v 3`\n - Printing a Photo to a printer with a pin that is not the default (1111) `python3 -m instax.print myPhoto.jpg -i 1234`\n\n### Hints and tips:\n - Make sure you are connected to the correct wifi network, once the printer is turned on, there will be an SSID / WiFi network available that starts with `INSTAX-` followed by 8 numbers. You'll need to connect to this.\n - If you have a static IP address set up on your computer, you'll need to turn on DHCP before attempting to print, the Instax printer will automatically assign you a new address once you connect.\n- Some Unix based operating systems may require you to use sudo in order to access the network.\n- The printer will automatically turn itself off after roughly 10 minutes of innactivity.\n- The instax.print utility will attempt to automatically rotate the image so that it either is correctly printed in portrait, or landscape with the thick bottom edge of the print on the left. If you wish to print your photos in a specific orientation that differs from this, then it's reccomended that you orient your photo in a tool like GIMP first, then strip out the rotation metadata. Once the rotation metadata has been stripped, the photo will need to be in a portrait orientation relative to the finished print (e.g. thick edge at the bottom). \n\n## Install Manually\n\n```\ngit clone https://github.com/jpwsutton/instax_api.git\ncd instax_api\npython3 setup.py install\n```\n",
    'author': 'James Sutton',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
