"""Wheels are elements of the MARK machines which take ints and return ints."""

from minisculus.wheel._abstract_processor import AbstractProcessor
from minisculus.wheel._abstract_wheel import AbstractWheel
from minisculus.wheel._incremental_factor_wheel import IncrementalFactorWheel
from minisculus.wheel._incremental_wheel import IncrementalWheel
from minisculus.wheel._optimized_wheel_chain import OptimizedWheelChain
from minisculus.wheel._wheel_chain import WheelChain

__all__ = [
    "AbstractProcessor",
    "AbstractWheel",
    "IncrementalWheel",
    "IncrementalFactorWheel",
    "OptimizedWheelChain",
    "WheelChain",
]
