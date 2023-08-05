# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kilroy_module_huggingface',
 'kilroy_module_huggingface.models',
 'kilroy_module_huggingface.resources']

package_data = \
{'': ['*']}

install_requires = \
['kilroy-module-pytorch-py-sdk>=0.8,<0.9',
 'omegaconf>=2.2,<3.0',
 'platformdirs>=2.5,<3.0',
 'pydantic[dotenv]>=1.10,<2.0',
 'transformers>=4.21,<5.0',
 'typer[all]>=0.6,<0.7']

entry_points = \
{'console_scripts': ['kilroy-module-huggingface = '
                     'kilroy_module_huggingface.__main__:cli']}

setup_kwargs = {
    'name': 'kilroy-module-huggingface',
    'version': '0.7.3',
    'description': 'kilroy module using Hugging Face models 🤗',
    'long_description': '<h1 align="center">kilroy-module-huggingface</h1>\n\n<div align="center">\n\nkilroy module using Hugging Face models 🤗\n\n[![Lint](https://github.com/kilroybot/kilroy-module-huggingface/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-huggingface/actions/workflows/lint.yaml)\n[![Multiplatform tests](https://github.com/kilroybot/kilroy-module-huggingface/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-huggingface/actions/workflows/test-multiplatform.yaml)\n[![Docker tests](https://github.com/kilroybot/kilroy-module-huggingface/actions/workflows/test-docker.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-huggingface/actions/workflows/test-docker.yaml)\n[![Docs](https://github.com/kilroybot/kilroy-module-huggingface/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-huggingface/actions/workflows/docs.yaml)\n\n</div>\n\n---\n\n## Installing\n\nUsing `pip`:\n\n```sh\npip install kilroy-module-huggingface\n```\n\n## Usage\n\nTo run the module server, install the package and run the following command:\n\n```sh\nkilroy-module-huggingface\n```\n\nThis will start the face server on port 11000 by default.\nThen you can communicate with the server, for example by using\n[this package](https://github.com/kilroybot/kilroy-module-client-py-sdk).\n',
    'author': 'kilroy',
    'author_email': 'kilroymail@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kilroybot/kilroy-module-huggingface',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
