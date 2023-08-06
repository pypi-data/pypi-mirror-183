"""Common sub metrics that are used internally at MongoDB."""

import multiprocessing
import os
import socket
from typing import Optional

import distro
import git
from mongo_tooling_metrics.base_models import SubMetrics


class HostInfo(SubMetrics):
    """Class to store host information."""

    ip_address: Optional[str]
    host_os: str
    num_cores: int
    memory: Optional[float]

    @classmethod
    def generate_metrics(cls):  # pylint: disable=arguments-differ
        """Get the host info to the best of our ability."""
        try:
            ip_address = socket.gethostbyname(socket.gethostname())
        except:
            ip_address = None
        try:
            memory = cls._get_memory()
        except:
            memory = None
        return cls(
            ip_address=ip_address,
            host_os=distro.name(pretty=True),
            num_cores=multiprocessing.cpu_count(),
            memory=memory,
        )

    @staticmethod
    def _get_memory():
        """Get total memory of the host system."""
        return os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') / (1024.**3)

    def is_malformed(self) -> bool:
        """Confirm whether this instance has all expected fields."""
        return None in [self.memory, self.ip_address]


class GitInfo(SubMetrics):
    """Class to store git repo information."""

    filepath: str
    commit_hash: Optional[str]
    branch_name: Optional[str]
    repo_name: Optional[str]

    @classmethod
    def generate_metrics(cls, filepath: str):  # pylint: disable=arguments-differ
        """Get the git info for a repo to the best of our ability."""
        try:
            commit_hash = git.Repo(filepath).head.commit.hexsha
        except:
            commit_hash = None
        try:
            if git.Repo(filepath).head.is_detached:
                branch_name = commit_hash
            else:
                branch_name = git.Repo(filepath).active_branch.name
        except:
            branch_name = None
        try:
            repo_name = git.Repo(filepath).working_tree_dir.split("/")[-1]
        except:
            repo_name = None
        return cls(
            filepath=filepath,
            commit_hash=commit_hash,
            branch_name=branch_name,
            repo_name=repo_name,
        )

    def is_malformed(self) -> bool:
        """Confirm whether this instance has all expected fields."""
        return None in [self.commit_hash, self.branch_name, self.repo_name]


MODULES_FILEPATH = 'src/mongo/db/modules'


def get_modules_git_info():
    """Get git info for all modules."""
    module_git_info = []
    try:
        module_git_info = [
            GitInfo.generate_metrics(os.path.join(MODULES_FILEPATH, module))
            for module in os.listdir(MODULES_FILEPATH)
            if os.path.isdir(os.path.join(MODULES_FILEPATH, module))
        ]
    except:
        pass
    return module_git_info
