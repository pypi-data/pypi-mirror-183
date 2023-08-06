#!/usr/bin/env python
import sys

import click

from gitlab_mr_note.config import GitlabConfig
from gitlab_mr_note.core import post_comment


@click.command()
@click.option("--server-url", "-s", help="Server URL of gitlab instance")
@click.option("--mr-id", "-m", help="ID of the MR to comment on")
@click.option("--project-id", "-p", help="ID of the Project")
@click.option("--job-name", "-j", help="Job Name")
@click.option("--private-token", "-t", help="Private Token")
def main(*args, **kwargs):
    gitlab_config = GitlabConfig(**kwargs)
    post_comment(gitlab_config, sys.stdin.read())


if __name__ == "__main__":
    main()
