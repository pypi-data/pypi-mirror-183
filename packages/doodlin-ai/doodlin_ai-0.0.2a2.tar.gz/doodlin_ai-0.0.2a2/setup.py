# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['doodlin_ai', 'doodlin_ai.datasets', 'doodlin_ai.models']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.26.37,<2.0.0',
 'huggingface>=0.0.1,<0.0.2',
 'moto[all]>=4.0.12,<5.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pillow>=9.3.0,<10.0.0',
 'pre-commit>=2.21.0,<3.0.0',
 'tqdm>=4.64.1,<5.0.0',
 'types-pillow>=9.3.0.4,<10.0.0.0',
 'types-tqdm>=4.64.7.9,<5.0.0.0']

setup_kwargs = {
    'name': 'doodlin-ai',
    'version': '0.0.2a2',
    'description': 'Doodlin AI Archaiver',
    'long_description': "# doodlin-ai\n\n[![PyPI](https://img.shields.io/pypi/v/doodlin-ai?style=flat-square)](https://pypi.python.org/pypi/doodlin-ai/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/doodlin-ai?style=flat-square)](https://pypi.python.org/pypi/doodlin-ai/)\n[![PyPI - License](https://img.shields.io/pypi/l/doodlin-ai?style=flat-square)](https://pypi.python.org/pypi/doodlin-ai/)\n[![Coookiecutter - Wolt](https://img.shields.io/badge/cookiecutter-Wolt-00c2e8?style=flat-square&logo=cookiecutter&logoColor=D4AA00&link=https://github.com/woltapp/wolt-python-package-cookiecutter)](https://github.com/woltapp/wolt-python-package-cookiecutter)\n\n\n---\n\n**Documentation**: [https://doodlincorp.github.io/doodlin-ai](https://doodlincorp.github.io/doodlin-ai)\n\n**Source Code**: [https://github.com/doodlincorp/doodlin-ai](https://github.com/doodlincorp/doodlin-ai)\n\n**PyPI**: [https://pypi.org/project/doodlin-ai/](https://pypi.org/project/doodlin-ai/)\n\n---\n\nDoodlin AI Archaiver\n\n## Installation\n\n```sh\npip install doodlin-ai\n```\n\n## Development\n\n* Clone this repository\n* Requirements:\n  * [Poetry](https://python-poetry.org/)\n  * Python 3.7+\n* Create a virtual environment and install the dependencies\n\n```sh\npoetry install\n```\n\n* Activate the virtual environment\n\n```sh\npoetry shell\n```\n\n### Testing\n\n```sh\npytest\n```\n\n### Documentation\n\nThe documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings\n of the public signatures of the source code. The documentation is updated and published as a [Github project page\n ](https://pages.github.com/) automatically as part each release.\n\n### Releasing\n\nTrigger the [Draft release workflow](https://github.com/doodlincorp/doodlin-ai/actions/workflows/draft_release.yml)\n(press _Run workflow_). This will update the changelog & version and create a GitHub release which is in _Draft_ state.\n\nFind the draft release from the\n[GitHub releases](https://github.com/doodlincorp/doodlin-ai/releases) and publish it. When\n a release is published, it'll trigger [release](https://github.com/doodlincorp/doodlin-ai/blob/master/.github/workflows/release.yml) workflow which creates PyPI\n release and deploys updated documentation.\n\n### Pre-commit\n\nPre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality\n checks to make sure the changeset is in good shape before a commit/push happens.\n\nYou can install the hooks with (runs for each commit):\n\n```sh\npre-commit install\n```\n\nOr if you want them to run only for each push:\n\n```sh\npre-commit install -t pre-push\n```\n\nOr if you want e.g. want to run all checks manually for all files:\n\n```sh\npre-commit run --all-files\n```\n\n---\n\nThis project was generated using the [wolt-python-package-cookiecutter](https://github.com/woltapp/wolt-python-package-cookiecutter) template.\n",
    'author': '한일석',
    'author_email': 'x2ever.han@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://doodlincorp.github.io/doodlin-ai',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
