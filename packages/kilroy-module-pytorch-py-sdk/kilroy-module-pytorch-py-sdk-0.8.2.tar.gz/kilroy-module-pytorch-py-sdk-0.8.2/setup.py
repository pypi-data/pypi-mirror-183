# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kilroy_module_pytorch_py_sdk',
 'kilroy_module_pytorch_py_sdk.generator',
 'kilroy_module_pytorch_py_sdk.losses',
 'kilroy_module_pytorch_py_sdk.losses.distribution',
 'kilroy_module_pytorch_py_sdk.losses.policy',
 'kilroy_module_pytorch_py_sdk.losses.value',
 'kilroy_module_pytorch_py_sdk.models',
 'kilroy_module_pytorch_py_sdk.module',
 'kilroy_module_pytorch_py_sdk.optimizers',
 'kilroy_module_pytorch_py_sdk.regularizations',
 'kilroy_module_pytorch_py_sdk.regularizations.policy',
 'kilroy_module_pytorch_py_sdk.regularizations.policy.departure',
 'kilroy_module_pytorch_py_sdk.regularizations.policy.entropy',
 'kilroy_module_pytorch_py_sdk.resources',
 'kilroy_module_pytorch_py_sdk.scalers',
 'kilroy_module_pytorch_py_sdk.scalers.reward',
 'kilroy_module_pytorch_py_sdk.schedulers',
 'kilroy_module_pytorch_py_sdk.trainers',
 'kilroy_module_pytorch_py_sdk.trainers.ac',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.cache',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.methods',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.methods.bespo',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.methods.bespo.bootstrap',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.methods.bespo.bootstrap.stop',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.methods.bespo.stop',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.methods.bespo.stop.policy',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.methods.bespo.stop.value',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.methods.espo',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.methods.espo.stop',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.methods.espo.stop.policy',
 'kilroy_module_pytorch_py_sdk.trainers.ac.reinforced.methods.espo.stop.value',
 'kilroy_module_pytorch_py_sdk.trainers.ac.supervised',
 'kilroy_module_pytorch_py_sdk.trainers.ac.supervised.methods',
 'kilroy_module_pytorch_py_sdk.trainers.ac.supervised.methods.mbgd',
 'kilroy_module_pytorch_py_sdk.trainers.vanilla',
 'kilroy_module_pytorch_py_sdk.trainers.vanilla.reinforced',
 'kilroy_module_pytorch_py_sdk.trainers.vanilla.reinforced.methods',
 'kilroy_module_pytorch_py_sdk.trainers.vanilla.reinforced.methods.reinforce',
 'kilroy_module_pytorch_py_sdk.trainers.vanilla.supervised',
 'kilroy_module_pytorch_py_sdk.trainers.vanilla.supervised.methods',
 'kilroy_module_pytorch_py_sdk.trainers.vanilla.supervised.methods.mbgd']

package_data = \
{'': ['*']}

install_requires = \
['kilroy-module-server-py-sdk>=0.10,<0.11', 'numpy>=1,<2', 'torch>=1,<2']

setup_kwargs = {
    'name': 'kilroy-module-pytorch-py-sdk',
    'version': '0.8.2',
    'description': 'SDK for kilroy modules using PyTorch 🧰',
    'long_description': '<h1 align="center">kilroy-module-pytorch-py-sdk</h1>\n\n<div align="center">\n\nSDK for kilroy modules using PyTorch 🧰\n\n[![Lint](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/lint.yaml)\n[![Tests](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/test-multiplatform.yaml)\n[![Docs](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-module-pytorch-py-sdk/actions/workflows/docs.yaml)\n\n</div>\n\n---\n\n## Installing\n\nUsing `pip`:\n\n```sh\npip install kilroy-module-pytorch-py-sdk\n```\n\n## Usage\n\n```python\nfrom kilroy_module_pytorch_py_sdk import BasicModule, ModuleServer\n\nclass MyModule(BasicModule):\n    ... # Implement all necessary methods here\n\nmodule = await MyModule.build()\nserver = ModuleServer(module)\n\nawait server.run(host="0.0.0.0", port=11000)\n```\n',
    'author': 'kilroy',
    'author_email': 'kilroymail@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kilroybot/kilroy-module-pytorch-py-sdk',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
