# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jiav', 'jiav.api', 'jiav.api.backends', 'jiav.api.schemas', 'jiav.utils']

package_data = \
{'': ['*']}

install_requires = \
['colorlog>=6.7.0,<7.0.0',
 'iteration-utilities>=0.11.0,<0.12.0',
 'jira>=3.4.1,<4.0.0',
 'jsonschema>=4.17.3,<5.0.0',
 'prettytable>=3.5.0,<4.0.0',
 'pyyaml>=6.0,<7.0',
 'strictyaml>=1.6.2,<2.0.0']

entry_points = \
{'console_scripts': ['jiav = jiav:cli.main']}

setup_kwargs = {
    'name': 'jiav',
    'version': '0.1.1',
    'description': 'Jira Issues Auto Verification',
    'long_description': '# jiav\n\nThis repository is a **Proof of Concept.**\n\n## Limitations And Words Of Caution\n\n**This tool is only tested against self-hosted (data center version) Jira.**  \nI have no access to a cloud Jira instance.\n\nSince this tool executes commands locally, we should avoid trusting public comments as much as possible.  \nIt will default to scanning only private comments (regardless of the visibility group). It is possible to read from public comments **if you understand the potential risk, this might cause to your systems**.\n\nThe output of verification steps is also not uploaded as attachments by default because it is impossible to limit attachments\' visibility, refer to [JRASERVER-3893](https://jira.atlassian.com/browse/JRASERVER-3893). It is possible to attach the output **if you understand the potential risk, this might expose sensitive information**.\n\n## General\n\n![jiav flow](https://jiav.readthedocs.io/en/latest/_images/Flow.jpeg)\n\nJira Issues Auto Verification.  \nThis tool aims to provide an auto-verification framework for Jira issues.  \nUsers provide a YAML-formatted comment in Jira issues, and the tool will execute it.\nOn successful execution, the issue will move to the desired status.\n\nExample of a manifest:\n\n```yaml\n---\njiav:\n  verified_status: "Done" # Status has to be present in the project workflow\n  verification_steps:\n    - name: Check line exists in file\n      backend: line\n      path: /path/to/file\n      line: hello_world\n```\n\n`jiav` allows developers to build custom backends; refer to the [documentation guide](docs/source/developing_backends.rst).  \nAn example of a backends shipped externally:\n\n- [jiav-backend-ansible](https://github.com/vkhitrin/jiav-backend-ansible) **this is a risky backend since it allows users to run arbitrary code. Be cautious when enabling it.**\n- [jiav-backend-command](https://github.com/vkhitrin/jiav-backend-command) **This is a risky backend since it allows users to run arbitrary code. Be cautious when enabling it.**\n\n## Requirements\n\n`jiav` requires Python `>= 3.8`.\n\n## Documentation\n\nVisit <https://jiav.readthedocs.io>.\n\n## Installation\n\nInstall from remote:\n\n```bash\npip3 install jiav\n```\n\nInstall from the local repository:\n\n```bash\npip3 install .\n```\n\n## Usage\n\nAfter installing this tool `jiav` command is available.\n\nThere are several sub-commands available, to view them execute `jiav`:\n\n```bash\nusage: jiav [-v | --version] [-d | --debug] <command> [<args>]\n\nGlobal flags\n  -v --version  prints version\n  -d --debug   show debug\n\nAvailable commands\n  verify        Verifies issues\n  list-backends    List available backends\n  validate-manifest  Validate jiav manifest\n```\n\n### Verify\n\nAttempt to verify issues from a list of issues:\n\n```bash\njiav --debug verify --jira=\'<JIRA_URL>\' --access-token=\'<ACCESS_TOKEN>\' --issue=\'<KEY-1>\' --issue=\'<KEY-2>\'\n```\n\nAttempt to verify issues from a JQL and output the result in JSON format:\n\n```bash\njiav --debug verify --jira=\'<JIRA_URL>\' --access-token=\'<ACCESS_TOKEN>\' --query=\'issue = "KEY-1"\' --format=\'json\'\n```\n\n### List backends\n\nList installed backends:\n\n```bash\njiav list-backends\n```\n\n### Validate manifest\n\nValidate `jiav` manifest from a file:\n\n```bash\njiav —debug validate-manifest —from-file=/path/to/file\n```\n\n## Contributing\n\n**All contributions are welcome!**\n\nTo install in development mode, use `poetry`:\n\n```bash\npip3 install poetry\npoetry install --with=main,dev\n```\n\nIf proposing new pull requests, please ensure that new/existing tests are passing:\n\n```bash\npytest\n```\n',
    'author': 'Vadim Khitrin',
    'author_email': 'me@vkhitrin.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/vkhitrin/jiav',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
