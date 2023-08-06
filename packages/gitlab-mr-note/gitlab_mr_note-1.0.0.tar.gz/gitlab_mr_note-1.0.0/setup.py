# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitlab_mr_note']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'python-gitlab>=3.12.0,<4.0.0']

entry_points = \
{'console_scripts': ['gitlab-mr-note = gitlab_mr_note.cli:main']}

setup_kwargs = {
    'name': 'gitlab-mr-note',
    'version': '1.0.0',
    'description': '',
    'long_description': '# Post or Update Comments on Gitlab MR\n\nThe idea behind this project is to post content on the Gitlab MR which\ndynamically updates as new commits are made. In order to do that, we add a\ncomment at the start of our content to identify the job the content is from.\n\n## Usage\n\n- General Access Token from `Settings > Access Tokens` with `api` permissions.\n- Go to `Settings > CI/CD > Variables > Add Variables`\n- Set the key to `GITLAB_PRIVATE_TOKEN` and value to key generated in first step.\n- Set `Mask` flag and uncheck `Protect` flag.\n- Create a test like follows\n\n```yaml\ntest:\n  stage: test\n  script:\n    - pip install gitlab-mr-note\n    - echo hello world | gitlab-mr-note\n  only:\n    - merge_requests\n```\n\n`gitlab-mr-note` infers the details from environment variables set in the CI.\nFor manual usage, pass the following args.\n\n```\nUsage: gitlab-mr-note [OPTIONS]\n\nOptions:\n  -s, --server-url TEXT     Server URL of gitlab instance\n  -m, --mr-id TEXT          ID of the MR to comment on\n  -p, --project-id TEXT     ID of the Project\n  -j, --job-name TEXT       Job Name\n  -t, --private-token TEXT  Private Token\n  --help                    Show this message and exit.\n```\n',
    'author': 'Irene',
    'author_email': 'irene@wn.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
