# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mltz_base']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.0', 'pandas>=1.4.0']

setup_kwargs = {
    'name': 'mltz-base',
    'version': '0.1.22',
    'description': 'Base Package for ML related dev',
    'long_description': '\n[![codecov](https://codecov.io/github/tzoght/mltz-base/branch/main/graph/badge.svg?token=UB03POGOUB)](https://codecov.io/github/tzoght/mltz-base)\n[![ci-cd](https://github.com/tzoght/mltz-base/actions/workflows/ci-cd.yml/badge.svg?branch=main)](https://github.com/tzoght/mltz-base/actions/workflows/ci-cd.yml) [![Documentation Status](https://readthedocs.org/projects/mltz-base/badge/?version=latest)](https://mltz-base.readthedocs.io/en/latest/?badge=latest) ![PyPI](https://img.shields.io/pypi/v/mltz_base)\n\n# mltz_base\n\nBase Package for ML related dev\n\n## Installation\n\n```bash\n$ pip install mltz_base\n```\nfrom  [Pypi repo](https://pypi.org/manage/project/mltz-base/releases/)\n\n## Usage\n\n- Coming soon\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`mltz_base` was created by Tony Zoght. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`mltz_base` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n\n\n## Code Coverage\n* [CodeCov](https://app.codecov.io/github/tzoght/mltz-base) \n',
    'author': 'Tony Zoght',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
