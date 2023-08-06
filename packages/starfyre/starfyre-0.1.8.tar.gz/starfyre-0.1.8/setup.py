# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starfyre']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'starfyre',
    'version': '0.1.8',
    'description': '',
    'long_description': '# Starfyre ⭐🔥\n\n## Introduction:\n\nStarfyre is a library that allows you to build reactive frontends using only Python. It is built using pyodide and wasm, which enables it to run natively in the browser. With Starfyre, you can create interactive, real-time applications with minimal effort. Simply define your frontend as a collection of observables and reactive functions, and let Starfyre handle the rest.\n\nPlease note that Starfyre is still very naive and may be buggy, as it was developed in just five days. However, it is under active development and we welcome contributions to improve it. Whether you are a seasoned web developer or new to frontend development, we hope that you will find Starfyre to be a useful tool. Its intuitive API and simple, declarative style make it easy to get started, and its powerful features allow you to build sophisticated applications.\n\n\n## Installation:\n\nThe easiest way to get started is to use `create-starfyre-app` repo. Hosted at [create-starfyre-app](https://github.com/sansyrox/create-starfyre-app)\n\n## Feedback\n\nFeel free to open an issue and let me know what you think of it. \n',
    'author': 'Sanskar Jethi',
    'author_email': 'sansyrox@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
