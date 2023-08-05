# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src', 'cz_gitmoji': 'src/cz_gitmoji', 'gitmojify': 'src/gitmojify'}

packages = \
['cz_gitmoji', 'gitmojify', 'shared']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=22.2.0,<23.0.0', 'commitizen>=2.38.0,<3.0.0']

entry_points = \
{'console_scripts': ['gitmojify = gitmojify.mojify:run']}

setup_kwargs = {
    'name': 'commitizen-gitmoji',
    'version': '0.1.1',
    'description': 'A commitizen plugin that combines gitmoji and conventional.',
    'long_description': '# cz-conventional-gitmoji\n\nA [commitizen](https://github.com/commitizen-tools/commitizen) plugin that combines [gitmoji](https://gitmoji.dev/) and [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/).\n\n## Installation\n\n```bash\npoetry add cz-conventional-gitmoji\n```\n\nor with pip:\n\n```bash\npip install cz-conventional-gitmoji\n```\n\n## Usage\n\nThis package can be used as a normal `commitizen` plugin, either by specifying the name on the command line\n\n```bash\ncz --name cz_gitmoji commit\n```\n\nor by setting it in your **pyproject.toml**\n\n```toml\n[tool.commitizen]\nname = "cz_gitmoji"\n```\n\nThis will make `commitizen` use the commit message parsing rules defined by this plugin, which are 100% compatible with [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/). As such, the gitmojis are completely optional and all commands will continue to validate commit messages in conventional format just fine. This is useful if you\'re transitioning an existing repo to `contentional-gitmoji` or you work in a team in which some colleagues don\'t like gitmojis.\n\n### gitmojify\n\nApart from the conventional-gitmoji rules, this package provides the `gitmojify` command which is also available as a pre-commit hook. The command reads a commit message either from cli or a commit message file and prepends the correct gitmoji based on the type. If the message already has a gitmoji, it is returned as is.\n\n```bash\n$ gitmojify -m "init: initial version"\n🎉 init: initial version\n```\n\nTo use it as a pre-commit hook, install this packages as well as `commitizen` and put the following into your **.pre-commit-config.yaml**\n\n```yaml\nrepos:\n  - repo: https://github.com/ljnsn/cz-conventional-gitmoji\n    rev: main\n    hooks:\n      - id: conventional-gitmoji\n```\n\nCommit with a message in conventional format that contains a valid type mapped by conventional gitmoji and the gitmoji will automagically be added.\n\n## Features\n\n- [x] Enable conventional gitmoji commit messages via `cz commit`.\n- [ ] Add `--simple-emojis` option to use only the emojis relating to `cz_conventional_commits` types.\n- [ ] Add `--simple-types` option to use only the types used by `cz_conventional_commits`.\n- [ ] Add `--conventional` option to put the emoji in the commit message, making it compatible with `cz_conventional_commits`.\n- [x] Add hook to automatically prepend the appropriate gitmoji for the commit\'s type.\n\n## Inspiration\n\n- [`commitizen-emoji`](https://github.com/marcelomaia/commitizen-emoji)\n',
    'author': 'ljnsn',
    'author_email': '82611987+ljnsn@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ljnsn/cz-conventional-gitmoji',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
