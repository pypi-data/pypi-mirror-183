from __future__ import annotations
from abc import abstractmethod
from typing import Any, Callable
from pydantic import BaseModel, Field, validate_model

from mongo_tooling_metrics.errors import InvalidMetricsSetup


class TopLevelMetrics(BaseModel):
    """Base class for a top-level metrics objects."""

    @classmethod
    @abstractmethod
    def generate_metrics(cls, *args, **kwargs) -> TopLevelMetrics:
        """Class method to generate this metrics object -- will be executed before process exit."""
        raise InvalidMetricsSetup(
            "'generate_metrics' will be used to construct the top-level metrics object and must be defined."
        )

    @staticmethod
    @abstractmethod
    def should_collect_metrics() -> bool:
        """Determine whether metrics collection should even be registered or not."""
        raise InvalidMetricsSetup(
            "'should_collect_metrics' is called when registering a new metrics object and must be defined."
        )

    @staticmethod
    def initialize_hooks() -> None:
        """Initialize any hooks that these metrics rely on here -- this will get called after the metrics are registered."""
        pass

    def is_malformed(self) -> bool:
        """Determine whether these metrics are malformed (have all expected fields/data)."""
        return False


class SubMetrics(BaseModel):
    """Base class for sub-level metrics objects."""

    @classmethod
    @abstractmethod
    def generate_metrics(cls, *args, **kwargs) -> SubMetrics:
        """Class method to generate this metrics object -- will be executed before process exit."""
        raise InvalidMetricsSetup(
            "'generate_metrics' should be used to construct the sub-metrics object and must be defined."
        )

    def is_malformed(self) -> bool:
        """Determine whether these metrics are malformed (have all expected fields/data)."""
        return False


class BaseHook(BaseModel):
    """Base class for hooks to collect intra-run function metrics."""

    original_fn: Callable[..., Any] = Field(..., exclude=True)

    @abstractmethod
    def passthrough_logic(self, *args, **kwargs) -> None:
        """Execute logic before calling the original function."""
        raise InvalidMetricsSetup(
            "'passthrough_logic' is called before calling the original function and must be defined."
        )

    def __call__(self, *args, **kwargs):
        """Call 'passthrough_logic' with **kwargs then call the 'original_fn' with **kwargs."""
        self.passthrough_logic(*args, **kwargs)
        self.original_fn(*args, **kwargs)

    def is_malformed(self) -> bool:
        """Make sure the hook still matches the pydantic model -- typing is not enforced intrarun by default."""
        *_, validation_error = validate_model(self.__class__, self.__dict__)
        return True if validation_error else False
