"""This is a sample metrics class used for testing & example sake."""
import sys
from typing import Optional
from mongo_tooling_metrics import get_hook, register_hook
from mongo_tooling_metrics.base_models import SubMetrics, TopLevelMetrics
from mongo_tooling_metrics.lib.hooks import ExitHook
from mongo_tooling_metrics.lib.sub_metrics import GitInfo, HostInfo


class BasicMetrics(TopLevelMetrics):
    """Collect basic metrics on the host machine."""
    host_info: HostInfo
    git_info: GitInfo
    exit_code: Optional[int]

    @classmethod
    def generate_metrics(cls) -> TopLevelMetrics:
        exit_hook = get_hook(ExitHook)
        return cls(
            host_info=HostInfo.generate_metrics(),
            git_info=GitInfo.generate_metrics('.'),
            exit_code=None if exit_hook.is_malformed() else exit_hook.exit_code,
        )

    @staticmethod
    def should_collect_metrics() -> bool:
        """Collect basic metrics at all times."""
        return True

    @staticmethod
    def initialize_hooks() -> None:
        """Initialize the exit hook bc the exit code is needed for these metrics."""
        sys.exit = register_hook(ExitHook(original_fn=sys.exit))

    def is_malformed(self) -> bool:
        """Return 'False' if the 'exit_code' is 'None' -- indicating the hook is malformed."""
        return self.exit_code == None
