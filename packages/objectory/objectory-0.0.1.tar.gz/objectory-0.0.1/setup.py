# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['objectory', 'objectory.utils']

package_data = \
{'': ['*']}

install_requires = \
['tornado>=6.0,<7.0']

setup_kwargs = {
    'name': 'objectory',
    'version': '0.0.1',
    'description': 'A light library for general purpose object factories',
    'long_description': '# objectory = object + factory\n\n<p align="center">\n   <a href="https://github.com/durandtibo/objectory/actions">\n      <img alt="CI" src="https://github.com/durandtibo/objectory/workflows/CI/badge.svg?event=push&branch=main">\n   </a>\n    <a href="https://pypi.org/project/objectory/">\n      <img alt="PYPI version" src="https://img.shields.io/pypi/v/objectory">\n    </a>\n   <a href="https://pypi.org/project/objectory/">\n      <img alt="Python" src="https://img.shields.io/pypi/pyversions/objectory.svg">\n   </a>\n   <a href="https://opensource.org/licenses/BSD-3-Clause">\n      <img alt="BSD-3-Clause" src="https://img.shields.io/pypi/l/objectory">\n   </a>\n   <a href="https://codecov.io/gh/durandtibo/objectory">\n      <img alt="Codecov" src="https://codecov.io/gh/durandtibo/objectory/branch/main/graph/badge.svg">\n   </a>\n   <a href="https://github.com/psf/black">\n     <img  alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">\n   </a>\n   <a href="https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings">\n     <img  alt="Doc style: google" src="https://img.shields.io/badge/%20style-google-3666d6.svg">\n   </a>\n   <br/>\n</p>\n\n## Overview\n\nA light Python library for general purpose object factories.\nIn particular, it focuses on dynamic object factory implementations where objects can be registered\ndynamically without changing the code of the factory.\nAn object factory can be used to instantiate an object from its configuration.\nThe current implementation contains both abstract factory and registry approaches.\n\n**factory**\n\n```python\nfrom objectory import factory\n\n\nclass MyClass:\n    pass\n\n\nobj = factory("MyClass")\nprint(obj)\n```\n\n**[abstract factory](https://durandtibo.github.io/objectory/abstract_factory/)**\n\n```python\nfrom objectory import AbstractFactory\n\n\nclass BaseClass(metaclass=AbstractFactory):\n    pass\n\n\nclass MyClass(BaseClass):\n    pass\n\n\nobj = BaseClass.factory("MyClass")\nprint(obj)\n```\n\n*Output*:\n\n```textmate\n<__main__.MyClass object at 0x123456789>\n```\n\n**[registry](https://durandtibo.github.io/objectory/registry/)**\n\n```python\nfrom objectory import Registry\n\nregistry = Registry()\n\n\n@registry.register()\nclass MyClass:\n    pass\n\n\nobj = registry.factory("MyClass")\nprint(obj)\n```\n\n```textmate\n<__main__.MyClass object at 0x123456789>\n```\n\nPlease read the [documentation](https://durandtibo.github.io/objectory/) to learn more about these\napproaches.\n\n- [Documentation](https://durandtibo.github.io/objectory/)\n- [Installation](#installation)\n- [Contributing](#contributing)\n- [API stability](#api-stability)\n- [License](#license)\n\n## Installation\n\nWe highly recommend installing\na [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).\n`objectory` can be installed from pip using the following command:\n\n```shell\npip install objectory\n```\n\nPlease check the [get started page](https://durandtibo.github.io/objectory/get_started) to see other\nalternatives to install the library.\n\n## Contributing\n\nPlease let us know if you encounter a bug by filing an issue.\n\nWe welcome contributions from anyone, even if you are new to open source.\n\n- If you are planning to contribute back bug-fixes, please do so without any further discussion.\n- If you plan to contribute new features, utility functions, or extensions to the core, please first\n  open an issue and discuss the feature with us.\n\nOnce you implement and test your feature or bug-fix, please submit a Pull Request.\n\nPlease feel free to open an issue to share your feedback or to request new features.\n\n## API stability\n\n:warning: While `objectory` is in development stage, no API is guaranteed to be stable from one\nrelease to the next.\nIn fact, it is very likely that the API will change multiple times before a stable 1.0.0 release.\nIn practice, this means that upgrading `objectory` to a new version will possibly break any code\nthat\nwas using the old version of `objectory`.\n\n## License\n\n`objectory` is licensed under BSD 3-Clause "New" or "Revised" license available\nin [LICENSE](LICENSE)\nfile.\n',
    'author': 'Thibaut Durand',
    'author_email': 'durand.tibo+gh@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/durandtibo/objectory',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
