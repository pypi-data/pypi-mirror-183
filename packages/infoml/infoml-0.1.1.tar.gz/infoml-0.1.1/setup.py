# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['infoml']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'infoml',
    'version': '0.1.1',
    'description': 'Python package for bioinformatics analysis and machine learning.',
    'long_description': '# infoml\n\nPython package for bioinformatics analysis and machine learning.\n\n## Installation\n\n```bash\n$ pip install infoml\n```\n\n## Usage\n\n- TODO\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that\nthis project is released with a Code of Conduct. By contributing to this project, you\nagree to abide by its terms.\n\n## License\n\n`infoml` was created by Tony Kabilan Okeke. It is licensed under the terms of the MIT \nlicense.\n\n## Credits\n\n`infoml` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) \nand the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n\n',
    'author': 'Tony Kabilan Okeke',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
