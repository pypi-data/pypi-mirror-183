import argparse
import logging
import subprocess
from rctl.cli.command import CmdBase

from rctl.cli.utils import fix_subparsers

logger = logging.getLogger(__name__)

class CmdPutFile(CmdBase):
    def __init__(self, args):
        super().__init__(args)
    def run(self):
        result = subprocess.run(["dvc", "pull"], capture_output=True)
        print(result.stdout)
        print(result.stderr)
        return 0


def add_parser(subparsers, parent_parser):
    REPO_HELP = "Get Files or folders. Use: `rctl get_files`"
    REPO_DESCRIPTION = (
        "Get Files or folders. Use: `rctl get_files`"
    )

    repo_parser = subparsers.add_parser(
        "get_files",
        parents=[parent_parser],
        description=REPO_DESCRIPTION,
        help=REPO_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    repo_parser.set_defaults(func=CmdPutFile)
