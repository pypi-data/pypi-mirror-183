# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sonicare_ble']

package_data = \
{'': ['*']}

install_requires = \
['bluetooth-data-tools>=0.1.2',
 'bluetooth-sensor-state-data>=1.6.0',
 'home-assistant-bluetooth>=1.6.0']

extras_require = \
{'docs': ['Sphinx>=5.0,<6.0',
          'sphinx-rtd-theme>=1.0,<2.0',
          'myst-parser>=0.18,<0.19']}

setup_kwargs = {
    'name': 'sonicare-ble',
    'version': '0.0.1',
    'description': 'Bluetooth library for Sonicare devices',
    'long_description': '# SONICARE BLE\n\nBluetooth library for Sonicare devices\n\n## Installation\n\nInstall this via pip (or your favourite package manager):\n\n`pip install sonicare-ble`\n',
    'author': 'Nubicula',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/nubicula/sonicare-ble',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
