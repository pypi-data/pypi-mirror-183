import argparse
import logging
import os
import subprocess
from rctl.cli.command import CmdBase

from rctl.cli.utils import fix_subparsers
import platform

logger = logging.getLogger(__name__)

class CmdRepo(CmdBase):
    def __init__(self, args):
        super().__init__(args)
        if getattr(self.args, "name", None):
            self.args.name = self.args.name.lower()


class CmdRepoCreate(CmdRepo):
    def run(self):
        repository_name = self.args.name
        print("repository_name " + repository_name)
        if platform.system() == 'Windows':
            result = subprocess.run(["{0} mb --with-lock local/{1}".format(self.args.mc_path, repository_name)], capture_output=True, shell=True)
        else:
            result = subprocess.run(["mc mb --with-lock local/{}".format(repository_name)], capture_output=True, shell=True)
        print(result.stderr)
        print(result.stdout)

        result = subprocess.run([f"gh repo create {repository_name} --private --clone" ], capture_output=True, shell=True, env=dict(os.environ, GH_TOKEN=os.environ.get("GH_TOKEN")))
        print(result.stderr)
        print(result.stdout)

        result = subprocess.run(["ls -l"], capture_output=True, shell=True)
        print(result.stdout)
        print(result.stderr)

        result = subprocess.run(["dvc init"], capture_output=True, shell=True, cwd=repository_name)
        print(result.stderr)
        print(result.stdout)

        result = subprocess.run(["git status"], capture_output=True, shell=True, cwd=repository_name)
        print(result.stderr)
        print(result.stdout)
    
        result = subprocess.run(["git commit -m 'Init DVC' -a"], capture_output=True, shell=True, cwd=repository_name)
        print(result.stderr)
        print(result.stdout)

        result = subprocess.run(["git push --set-upstream origin main"], capture_output=True, shell=True, cwd=repository_name)
        print(result.stderr)
        print(result.stdout)

        result = subprocess.run([f"dvc remote add -d minio s3://{repository_name} -f"], capture_output=True, shell=True, cwd=repository_name)
        print(result.stderr)
        print(result.stdout)

        result = subprocess.run(["dvc remote modify minio endpointurl http://127.0.0.1:9000/"],
                                capture_output=True, shell=True, cwd=repository_name)
        print(result.stderr)
        print(result.stdout)

        result = subprocess.run(["dvc remote modify minio secret_access_key minioadmin"],
                                capture_output=True, shell=True, cwd=repository_name)
        print(result.stderr)
        print(result.stdout)

        result = subprocess.run(["dvc remote modify minio access_key_id minioadmin"],
                                capture_output=True, shell=True, cwd=repository_name)
        print(result.stderr)
        print(result.stdout)

        result = subprocess.run(["dvc config core.autostage true"], capture_output=True, shell=True, cwd=repository_name)
        print(result.stderr)
        print(result.stdout)
        return 0


def add_parser(subparsers, parent_parser):
    REPO_HELP = "Create a new repository."
    REPO_DESCRIPTION = (
        "Create a new repository."
    )

    repo_parser = subparsers.add_parser(
        "repo_create",
        parents=[parent_parser],
        description=REPO_DESCRIPTION,
        help=REPO_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    repo_parser.add_argument(
        "name", nargs="?", help="Name of the remote",
    )

    repo_parser.add_argument(
        "mc_path", nargs="?", help="mc.exe Path of the minio cli",
    )
    
    repo_parser.set_defaults(func=CmdRepoCreate)
