import argparse
import logging
import subprocess
from rctl.cli.command import CmdBase

from rctl.cli.utils import fix_subparsers

logger = logging.getLogger(__name__)

class CmdRepo(CmdBase):
    def __init__(self, args):
        super().__init__(args)
        if getattr(self.args, "name", None):
            self.args.name = self.args.name.lower()


class CmdRepoCreate(CmdRepo):
    def run(self):
        result = subprocess.run(["git", "push"], capture_output=True)
        print(result.stderr)
        print(result.stdout)

        result = subprocess.run(["dvc", "push"], capture_output=True)
        print(result.stderr)
        print(result.stdout)
        return 0


def add_parser(subparsers, parent_parser):
    REPO_HELP = "Push"
    REPO_DESCRIPTION = (
        "Push"
    )

    repo_parser = subparsers.add_parser(
        "push",
        parents=[parent_parser],
        description=REPO_DESCRIPTION,
        help=REPO_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    
    repo_parser.set_defaults(func=CmdRepoCreate)
