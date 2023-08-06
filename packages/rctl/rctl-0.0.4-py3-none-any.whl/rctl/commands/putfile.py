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
        message = self.args.message
        path = self.args.path
        result = subprocess.run(["dvc", "add", f"{path}"], capture_output=True, shell=True)
        print(result.stdout)
        print(result.stderr)
        result = subprocess.run(["git", "add", "."], capture_output=True, shell=True)
        print(result.stderr)
        print(result.stdout)
        result = subprocess.run(["git", "commit", "-m", f"{message}", "-a"], capture_output=True, shell=True)
        print(result.stderr)
        print(result.stdout)
        result = subprocess.run(["git", "push"], capture_output=True, shell=True)
        print(result.stderr)
        print(result.stdout)

        result = subprocess.run(["dvc", "push"], capture_output=True, shell=True)
        print(result.stderr)
        print(result.stdout)
        return 0


def add_parser(subparsers, parent_parser):
    REPO_HELP = "Put Files or folders. Use: `rctl put_files <file or folder path> <commit message>`"
    REPO_DESCRIPTION = (
        "Put Files or folders. Use: `rctl put_files <file or folder path> <commit message>`"
    )

    repo_parser = subparsers.add_parser(
        "put_files",
        parents=[parent_parser],
        description=REPO_DESCRIPTION,
        help=REPO_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    repo_parser.add_argument(
        "path", nargs="?", help="File or Folder path",
    )

    repo_parser.add_argument(
        "message", nargs="?", help="Commit message",
    )
    
 
    
    repo_parser.set_defaults(func=CmdPutFile)
