# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['codewars_cli']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'click>=8.1.3,<9.0.0',
 'cloudscraper>=1.2.66,<2.0.0',
 'rich>=12.6.0,<13.0.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['codewars-cli = codewars_cli:main']}

setup_kwargs = {
    'name': 'codewars-cli',
    'version': '0.1.0',
    'description': 'An unofficial CLI for CodeWars.',
    'long_description': '# codewars-cli\nAn unofficial CLI for CodeWars.\n\n## Configuration\nYou need to set the `CW_SESSION_ID` and `CW_REMEMBER_USER_TOKEN` environment variables which you can grab from your cookies.\n\nRich will look at `MANPAGER` then the `PAGER` environment variables (`MANPAGER` takes priority) to get the pager command. On Linux and macOS you can set one of these to `less -r` to display the description with ANSI styles.\n\n## Installation\nYou can install `codewars-cli` using `pip`:\n```\npip install codewars-cli\n```\n\n## Usage\n```\n$ codewars-cli --help\nUsage: codewars-cli [OPTIONS] COMMAND [ARGS]...\n\n  An unofficial CLI for CodeWars.\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  attempt   Attempt to pass the full test suite.\n  practice  Search for a kata.\n  submit    Submit your solution.\n  test      Test against the sample tests.\n  train     Choose a kata to solve.\n```\nYou can do the same for each subcommand.\n',
    'author': 'Kappa',
    'author_email': 'f.cappetti.05@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kappq/codewars-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
