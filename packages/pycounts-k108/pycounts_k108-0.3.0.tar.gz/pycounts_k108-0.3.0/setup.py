# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pycounts_k108', 'pycounts_k108.data']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.2,<4.0.0']

setup_kwargs = {
    'name': 'pycounts-k108',
    'version': '0.3.0',
    'description': 'Calculate word counts in a text file!',
    'long_description': '# pycounts\n\n[![codecov](https://codecov.io/gh/Kabilan108/pycounts/branch/dev/graph/badge.svg?token=2CWJI58ASX)](https://codecov.io/gh/Kabilan108/pycounts)\n\nCalculate word counts in a text file!\n\n## Installation\n\n```bash\n$ pip install pycounts\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`pycounts` was created by Tony Kabilan Okeke. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`pycounts` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Tony Kabilan Okeke',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
