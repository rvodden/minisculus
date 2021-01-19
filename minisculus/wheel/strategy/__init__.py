"""A strategy takes a list of wheels and returns a shorter equivalent list."""

from minisculus.wheel.strategy._abstract_strategy import AbstractStrategy
from minisculus.wheel.strategy._merge_consecutive_incremental_factor_wheels import (
    MergeConsecutiveIncrementalFactorWheels,
)

__all__ = ["AbstractStrategy", "MergeConsecutiveIncrementalFactorWheels"]
