# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['full_apply']

package_data = \
{'': ['*']}

install_requires = \
['typer>=0.7.0,<0.8.0', 'yachalk>=0.1.5,<0.2.0']

entry_points = \
{'console_scripts': ['full-apply = full_apply.__main__:cli_main']}

setup_kwargs = {
    'name': 'full-apply',
    'version': '0.3.0',
    'description': 'Apply commands to both file contents and paths',
    'long_description': '# full-apply\n\nApply commands to both file contents and paths.\n\n## Installation\n\n```bash\npip3 install full-apply\n```\n\n## Usage\n\n```console\n$ full-apply --help\nUsage: full-apply [OPTIONS] CMD PATHS...\n\n  Apply commands to both file contents and paths.\n\n  File paths and contents will be piped into the given shell command\'s\n  standard input and replaced with its output.\n\n  Examples:\n\n  Replace all occurrences of "foo" with "bar" in both paths and file contents\n  within the current directory and sub-directories:\n\n    $ full-apply "sed s/foo/bar/g" .\n\nArguments:\n  CMD       shell command to apply  [required]\n  PATHS...  paths to apply to (recursively)  [required]\n\nOptions:\n  --yes / --no-yes        actually apply instead of performing a dry-run\n                          [default: no-yes]\n  --hidden / --no-hidden  whether to go through "hidden" (dot-prefixed) files\n                          [default: no-hidden]\n  --help                  Show this message and exit.\n```\n',
    'author': 'smheidrich',
    'author_email': 'smheidrich@weltenfunktion.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
