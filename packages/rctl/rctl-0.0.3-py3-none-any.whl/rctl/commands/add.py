import argparse
import logging
import subprocess
from rctl.cli.command import CmdBase

from rctl.cli.utils import fix_subparsers

logger = logging.getLogger(__name__)

class CmdAdd(CmdBase):
    def __init__(self, args):
        super().__init__(args)
    def run(self):
        path = self.args.path
        result = subprocess.run(["dvc", "add", f"{path}"], capture_output=True)
        print(result.stdout)
        print(result.stderr)
        result = subprocess.run(["git", "add", "."], capture_output=True)
        print(result.stderr)
        print(result.stdout)
        return 0


def add_parser(subparsers, parent_parser):
    REPO_HELP = "Add"
    REPO_DESCRIPTION = (
        "Add"
    )

    repo_parser = subparsers.add_parser(
        "add",
        parents=[parent_parser],
        description=REPO_DESCRIPTION,
        help=REPO_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    repo_parser.add_argument(
        "path", nargs="?", help="Path of Data",
    )
    
    repo_parser.set_defaults(func=CmdAdd)
