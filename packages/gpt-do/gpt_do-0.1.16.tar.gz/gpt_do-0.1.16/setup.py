# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gpt_do',
 'gpt_do.doers',
 'gpt_do.vendor.chatgpt_wrapper',
 'gpt_do.vendor.chatgpt_wrapper.chatgpt_wrapper']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'dirtyjson>=1.0.8,<2.0.0',
 'openai>=0.25.0,<0.26.0',
 'playwright>=1.29.0,<2.0.0',
 'py-getch>=1.0.1,<2.0.0',
 'retry>=0.9.2,<0.10.0',
 'rich>=12.6.0,<13.0.0']

entry_points = \
{'console_scripts': ['ddo = gpt_do.cli:do',
                     'do = gpt_do.cli:do',
                     'gpt-do = gpt_do.cli:do']}

setup_kwargs = {
    'name': 'gpt-do',
    'version': '0.1.16',
    'description': 'GPT-powered bash commands.',
    'long_description': '# `gpt-do`\n\nThis is a handy-dandy CLI for when you don\'t know wtf to do.\n\nInstead of furiously grepping through man pages, simply use `do` (or `ddo` if on `bash`/`zsh`), and have GPT-3 do all the magic for you.\n\nCheck out the blog post [here](https://musings.yasyf.com/never-write-a-bash-command-again-with-gpt-3/).\n\n## Demo\n\nClick to play:\n\n[![asciicast](https://asciinema.org/a/oXRkVfVsxvUFq4SFjrstgsZck.png)](https://asciinema.org/a/oXRkVfVsxvUFq4SFjrstgsZck?i=0.5&autoplay=1)\n\n## Installation\n\nWe recommend using [`pipx`](https://pypa.github.io/pipx/):\n\n```console\n$ pipx install gpt-do\n$ which do\n~/.local/bin/do\n```\n\nHowever you can also use `brew`:\n\n```console\n$ brew install yasyf/do/do\n$ which do\n/opt/homebrew/bin/do\n```\n\nOr `pip`:\n\n```console\n$ pip install gpt-do\n$ which do\n~/.asdf/installs/python/3.11.0/bin/do\n```\n\n## Usage\n\n**n.b.** If you\'re on `bash` or `zsh`, `do` is a reserved keyword, so you\'ll have to use the alias `ddo`.\n\n**n.b.** The default model used is **GPT-3**. Please ensure you have sufficient credits in your OpenAI account to use it.\n\n```console\n$ export OPENAI_API_KEY=xxx # stick this in your bash_profile\n$ do amend the message of my last commit to "It works!"\nThis command will amend the message of the last commit to \'It works!\'.\ngit commit --amend -m \'It works!\'\nDo you want to continue? [y/N]: y\n[main 3e6a2f6] It works!!\n Date: Thu Dec 22 01:15:40 2022 -0800\n 5 files changed, 1088 insertions(+)\n create mode 100644 .gitignore\n create mode 100644 .gitmodules\n create mode 100644 README.md\n create mode 100644 poetry.lock\n create mode 100644 pyproject.toml\n```\n',
    'author': 'Yasyf Mohamedali',
    'author_email': 'yasyfm@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/yasyf/gpt-do',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9.0,<4.0.0',
}


setup(**setup_kwargs)
