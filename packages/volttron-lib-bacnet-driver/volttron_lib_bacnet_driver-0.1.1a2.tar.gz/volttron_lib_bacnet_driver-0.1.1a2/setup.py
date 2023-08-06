# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['volttron', 'volttron.driver.interfaces.bacnet']

package_data = \
{'': ['*']}

install_requires = \
['bacpypes==0.16.7', 'volttron-lib-base-driver>=0.2.0rc0,<0.3.0']

setup_kwargs = {
    'name': 'volttron-lib-bacnet-driver',
    'version': '0.1.1a2',
    'description': 'BACnet driver supported and maintained by the Volttron team.',
    'long_description': '# volttron-lib-bacnet-driver\n\n[![Passing?](https://github.com/VOLTTRON/volttron-lib-bacnet-driver/actions/workflows/run-tests.yml/badge.svg)](https://github.com/VOLTTRON/volttron-lib-bacnet-driver/actions/workflows/run-tests.yml)\n[![pypi version](https://img.shields.io/pypi/v/volttron-lib-bacnet-driver.svg)](https://pypi.org/project/volttron-lib-bacnet-driver/)\n\n# Prerequisites\n\n* Python 3.8\n\n## Python\n\n<details>\n<summary>To install Python 3.8, we recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>\n\n```bash\n# install pyenv\ngit clone https://github.com/pyenv/pyenv ~/.pyenv\n\n# setup pyenv (you should also put these three lines in .bashrc or similar)\nexport PATH="${HOME}/.pyenv/bin:${PATH}"\nexport PYENV_ROOT="${HOME}/.pyenv"\neval "$(pyenv init -)"\n\n# install Python 3.8\npyenv install 3.8.10\n\n# make it available globally\npyenv global system 3.8.10\n```\n</details>\n\n\n## Poetry\n\nThis project uses `poetry` to install and manage dependencies. To install poetry,\nfollow these [instructions](https://python-poetry.org/docs/master/#installation).\n\n# Installation\n\n1. Create and activate a virtual environment.\n\n```shell\npython -m venv env\nsource env/bin/activate\n```\n\n2. Install volttron and start the platform.\n\n```shell\npip install volttron\n\n# Start platform with output going to volttron.log\nvolttron -vv -l volttron.log &\n```\n\n3. Install the volttron platform driver:\n\n```shell\nvctl install volttron-platform-driver --vip-identity platform.driver --start\n```\n\n4. Install the BACnetProxy agent:\n\n```shell\nvctl install volttron-bacnet-proxy --agent-config <path to bacnet proxy agent configuration file>\n```\n\n5.  Install the volttron bacnet driver library:\n\n```shell\npip install volttron-lib-bacnet-driver\n```\n\n6.  Install a BACnet Driver onto the Platform Driver.\n\nInstalling a BACnet driver in the Platform Driver Agent requires adding copies of the device configuration and registry configuration files to the Platform Driver’s configuration store.\n\nCreate a config directory and navigate to it:\n\n```shell\nmkdir config\ncd config\n```\nCreate a file called `bacnet.config`; it should contain a JSON object that specifies the configuration of your BACnet driver. The following JSON is an example:\n\n```json\n{\n    "driver_config": {"device_address": "123.45.67.890",\n                      "device_id": 123456},\n    "driver_type": "bacnet",\n    "registry_config":"config://bacnet.csv",\n    "interval": 15,\n    "timezone": "US/Pacific"\n}\n```\n\nCreate another file called `bacnet.csv`; it should contain all the points on the device that you want published to Volttron. The following CSV file is an example:\n\n```csv\nPoint Name,Volttron Point Name,Units,Unit Details,BACnet Object Type,Property,Writable,Index,Notes\n3820a/Field Bus.3820A CHILLER.AHU-COIL-CHWR-T,3820a/Field Bus.3820A CHILLER.AHU-COIL-CHWR-T,degreesFahrenheit,-50.00 to 250.00,analogInput,presentValue,FALSE,3000741,,Primary CHW Return Temp\n```\n\nAdd the bacnet driver config and bacnet csv file to the Platform Driver configuration store:\n\n```\nvctl config store platform.driver bacnet.csv bacnet.csv --csv\nvctl config store platform.driver devices/bacnet bacnet1.config\n```\n\n7. Observe Data\n\nTo see data being published to the bus, install a [Listener Agent](https://pypi.org/project/volttron-listener/):\n\n```\nvctl install volttron-listener --start\n```\n\nOnce installed, you should see the data being published by viewing the Volttron logs file that was created in step 2.\nTo watch the logs, open a separate terminal and run the following command:\n\n```\ntail -f <path to folder containing volttron.log>/volttron.log\n```\n\n# Development\n\nPlease see the following for contributing guidelines [contributing](https://github.com/eclipse-volttron/volttron-core/blob/develop/CONTRIBUTING.md).\n\nPlease see the following helpful guide about [developing modular VOLTTRON agents](https://github.com/eclipse-volttron/volttron-core/blob/develop/DEVELOPING_ON_MODULAR.md)\n\n# Disclaimer Notice\n\nThis material was prepared as an account of work sponsored by an agency of the\nUnited States Government.  Neither the United States Government nor the United\nStates Department of Energy, nor Battelle, nor any of their employees, nor any\njurisdiction or organization that has cooperated in the development of these\nmaterials, makes any warranty, express or implied, or assumes any legal\nliability or responsibility for the accuracy, completeness, or usefulness or any\ninformation, apparatus, product, software, or process disclosed, or represents\nthat its use would not infringe privately owned rights.\n\nReference herein to any specific commercial product, process, or service by\ntrade name, trademark, manufacturer, or otherwise does not necessarily\nconstitute or imply its endorsement, recommendation, or favoring by the United\nStates Government or any agency thereof, or Battelle Memorial Institute. The\nviews and opinions of authors expressed herein do not necessarily state or\nreflect those of the United States Government or any agency thereof.\n',
    'author': 'Mark Bonicillo',
    'author_email': 'volttron@pnnl.gov',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/eclipse-volttron/volttron-lib-bacnet-driver',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
