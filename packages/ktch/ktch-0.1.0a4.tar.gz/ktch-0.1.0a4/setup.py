# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ktch',
 'ktch.datasets',
 'ktch.datasets.data',
 'ktch.datasets.descr',
 'ktch.landmark',
 'ktch.landmark.tests',
 'ktch.outline',
 'ktch.outline._plot',
 'ktch.outline.tests',
 'ktch.tests']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23,<2.0',
 'pandas>=1.5.2,<2.0.0',
 'scikit-learn>=1.2,<2.0',
 'scipy>=1.8,<2.0']

setup_kwargs = {
    'name': 'ktch',
    'version': '0.1.0a4',
    'description': '**ktch** is a python package for model-based morphometrics.',
    'long_description': '# ktch - A python package for model-based morphometrics\n\n**ktch** is a python package for model-based morphometrics.\n\n\n## License\n\nktch is licensed under the Apache License, Version2.0\n',
    'author': 'Noshita, Koji',
    'author_email': 'noshita@morphometrics.jp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/noshita/ktch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
