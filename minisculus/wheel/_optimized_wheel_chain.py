from typing import List

from minisculus.wheel._abstract_wheel import AbstractWheel
from minisculus.wheel._wheel_chain import WheelChain
from minisculus.wheel.strategy import MergeConsecutiveIncrementalFactorWheels


class OptimizedWheelChain(WheelChain):
    """Processes indexes using a chain of wheels.

    The OptimizedWheelChain will automagically reduce the number of wheels
    to make processing time shorter.
    """

    def __init__(self, wheels: List[AbstractWheel]):
        wheels = MergeConsecutiveIncrementalFactorWheels.optimize(wheels)
        super().__init__(wheels)
