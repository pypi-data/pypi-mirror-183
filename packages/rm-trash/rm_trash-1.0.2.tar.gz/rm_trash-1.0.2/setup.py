# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['rm_trash']

package_data = \
{'': ['*']}

install_requires = \
['inflect>=6.0.2,<7.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['trash = rm_trash.trash:app']}

setup_kwargs = {
    'name': 'rm-trash',
    'version': '1.0.2',
    'description': '🗑 Safe(r) deletion of files from the macOS command line',
    'long_description': '# rm-trash\n\n[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/rm-trash?logo=github&color=orange&logoColor=white&style=for-the-badge)](https://github.com/celsiusnarhwal/rm-trash/releases)\n\nrm-trash is a macOS command-line utility that moves files and directories to the Trash.\nUnlike [similar](https://github.com/ali-rantakari/trash) [tools](https://github.com/sindresorhus/macos-trash),\nrm-trash intends to be a complete alternative to `rm` and `rmdir`, to the extent that you could use aliases\nto have rm-trash replace them both.\n\nrm-trash works by communicating with Finder\nthrough [AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html),\nso it\'s no different from moving files to the Trash\nfrom within Finder itself.\n\n## Installation\n\nInstall rm-trash with [Homebrew](https://brew.sh) via\nthe [Houkago Tea Tap](https://github.com/celsiusnarhwal/homebrew-htt).\n\n```bash\nbrew tap celsiusnarhwal/htt\nbrew install rm-trash\n```\n\n## Usage\n\nInvoke rm-trash with the `trash` command, which will become available after installation.\n\n```bash\ntrash --help\n```\n\nwill tell you everything you need to know.\n\n## Replacing `rm` and `rmdir`\n\nIf you wish, you can replace `rm` and `rmdir` with aliases to `trash`.\n\n```bash\nalias rm="trash trash"\nalias rmdir="trash dir"\n```\n\n`trash` supports all options of both commands. Run `trash --help` for details.\n\n## Limitations\n\nrm-trash refuses to as root when [System Integrity Protection](https://support.apple.com/en-us/HT204899) (SIP) is\ndisabled.\nYou can still run rm-trash as a non-root user when SIP is disabled, or as any user when SIP is enabled. This limitation\nis intended to prevent you from accidentally trashing files and directories that are typically protected by SIP.\n\nIf you must remove files as root while SIP is disabled, you can always fall back to `rm`.\n\n## License\n\nrm-trash is licensed under the [MIT License](LICENSE.md).',
    'author': 'celsius narhwal',
    'author_email': 'hello@celsiusnarhwal.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/celsiusnarhwal/rm-trash',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
