import argparse
import logging
import subprocess
from rctl.cli.command import CmdBase

from rctl.cli.utils import fix_subparsers

logger = logging.getLogger(__name__)

class CmdRepoCreate(CmdBase):
    def __init__(self, args):
        super().__init__(args)
    def run(self):
        message = self.args.message
        result = subprocess.run(["git", "commit", "-m", f"{message}", "-a"], capture_output=True)
        print(result.stderr)
        print(result.stdout)
        return 0


def add_parser(subparsers, parent_parser):
    REPO_HELP = "Commit"
    REPO_DESCRIPTION = (
        "Commit"
    )

    repo_parser = subparsers.add_parser(
        "commit",
        parents=[parent_parser],
        description=REPO_DESCRIPTION,
        help=REPO_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    repo_parser.add_argument(
        "message", nargs="?", help="Message",
    )
 
    
    repo_parser.set_defaults(func=CmdRepoCreate)
