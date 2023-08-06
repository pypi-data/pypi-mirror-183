# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_tmux']

package_data = \
{'': ['*']}

install_requires = \
['libtmux==0.16']

entry_points = \
{'pytest11': ['pytest-tmux = pytest_tmux.plugin']}

setup_kwargs = {
    'name': 'pytest-tmux',
    'version': '0.0.1',
    'description': 'A pytest plugin that enables tmux driven tests',
    'long_description': '# pytest-tmux\n\n[![PyPI version](https://img.shields.io/pypi/v/pytest-tmux.svg)](https://pypi.org/project/pytest-tmux)\n\n[![Python versions](https://img.shields.io/pypi/pyversions/pytest-tmux.svg)](https://pypi.org/project/pytest-tmux)\n\n[![See Build Status on AppVeyor](https://ci.appveyor.com/api/projects/status/github/rockandska/pytest-tmux?branch=master)](https://ci.appveyor.com/project/rockandska/pytest-tmux/branch/master)\n\nA pytest plugin that enables tmux driven tests\n\n------------------------------------------------------------------------\n\n## Features\n\n- Enable tmux driven tests\n- Enable screen assertion\n- Enable row assertion\n\n## Requirements\n\n- python >= 3.7\n- python libtmux==0.16\n- pytest\n- tmux\n\n## Installation\n\nYou can install "pytest-tmux" via [pip](https://pypi.org/project/pip/)\nfrom [PyPI](https://pypi.org/project):\n\n    $ pip install pytest-tmux\n\n## Purpose and design\n\nThis plugin is intend to help users who whant to test interrative cli.\nWhen using `tmux` fixture it basically :\n- create a tmux server (socket create in tmux tmpdir)\n- create a session automatically when requested with name based on the name of test file\n- create a window automatically when requested with name based on the name of the test\n\nConfiguration could be set on different level :\n- cli args (see --tmux-* switch with pytest --help)\n- at the test level with tmux_cfg marker\n- dynamically inside test with `tmux.set()`\n- using `tmux.screen() / tmux.row()` (timeout / delay)\n\n\n## Usage\n\n### Basic example\n\n#### Success\n\n#### Code\n```python\nimport pytest\nfrom inspect import cleandoc\n\ndef test_assert(tmux):\n    # Set some options before session / windows is started\n    tmux.set(window_command=\'env -i PS1="$ " TERM="xterm-256color" /usr/bin/env bash --norc --noprofile\')\n    assert tmux.screen() == \'$\'\n    tmux.send_keys(r\'printf "  Hello World  .\\n\\n"\')\n    expected=r"""\n    $ printf "  Hello World  .\\n\\n"\n      Hello World  .\n\n    $\n    """\n    assert tmux.screen() == cleandoc(expected)\n```\n\n### Failure\n\n#### Code\n```python\nimport pytest\nfrom inspect import cleandoc\n\ndef test_assert(tmux):\n    # Set some options before session / windows is started\n    tmux.set(window_command=\'env -i PS1="# " TERM="xterm-256color" /usr/bin/env bash --norc --noprofile\')\n    assert tmux.row(0) == \'$\'\n```\n\n#### Output\n\n```\n>       assert tmux.row(0) == \'$\'\nE       assert failed\nE         > Common line\nE         - Left\nE         + Right\nE         -------------\nE         - #\nE         + $\nE         -------------\n```\n\n### Waiting for a long process\n\n```python\nimport pytest\nfrom inspect import cleandoc\n\ndef test_assert(tmux):\n    # Set some options before session / windows is started\n    tmux.set(window_command=\'env -i PS1="$ " TERM="xterm-256color" /usr/bin/env bash --norc --noprofile\')\n    assert tmux.row(0) == \'$\'\n    tmux.send_keys(\'sleep 5\')\n    assert tmux.row(0) == \'$ sleep 5\'\n    expected = """\n    $ sleep 5\n    $\n    """\n    assert tmux.screen(timeout=6, delay=0.5) == cleandoc(expected)\n```\n\n### Debug\n\nIf needed, a debug mode is available with `--tmux-debug`.\nIt will prompt you to :\n- open the tmux session for the current test\n- press enter to continue on :\n    - send_keys\n    - kill_session\n\n## Contributing\n\nContributions are very welcome.\n\n### Dev requirements\n\n- minor python3 versions present in .python-version\n- pyenv > v2.3.9 ( optional but recommended )\n- virtualenv (will be installed by `make venv` if not available)\n\n### Start hacking\n\n#### Install python versions used for tests ( recommended )\n\n```shell\npyenv install\n```\n\n/!\\ Install multiple versions in a single command only available in pyenv > 2.3.9\n\n#### Create the project virtualenv\n\n```shell\n$ make venv\n```\n\nThis target does the following:\n\n- installs `virtualenv` if not found\n- creates a venv in `.venv` for `dev-requirements.txt`\n- installs `dev-requirements.txt`\n- creates a `.python-venv` symlink to `.venv/bin/activate`\n\n### Run tests\n\nTests are driven by tox / make\n\n#### Run with make\n\nExample:\n```shell\n$ make test\n```\n\n#### Run with tox or free commands\n\nExample:\n```shell\n$ source .python-venv\n$ tox\n$ poetry run pytest tests/\n```\n\n#### Formater\n\n`black` and `isort` run in check mode by default\n\ncheck mode could be removed by running the env as :\n```shell\n$ source .python-venv\n$ tox -e black --\n$ tox -e isort --\n```\n\n### Update tox.ini / pyproject.toml\n\n- Update `tox.ini.j2` to update `tox.ini`\n- Update `pyproject.ini.j2` to update `pyproject.ini`\n- Update `.python-version` to add a new python version (order is important)\n\n## License\n\nDistributed under the terms of the\n[MIT](http://opensource.org/licenses/MIT) license, "pytest-tmux" is free\nand open source software\n\n## Issues\n\nIf you encounter any problems, please [file an\nissue](https://github.com/rockandska/pytest-tmux/issues) along with a\ndetailed description.\n',
    'author': 'rockandska',
    'author_email': 'yoann_mac_donald@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<=3.11.9999',
}


setup(**setup_kwargs)
