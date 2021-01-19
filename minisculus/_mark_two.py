from pydantic import validate_arguments

from minisculus._single_processor_mark import SingleProcessorMark
from minisculus.wheel import (
    IncrementalFactorWheel,
    IncrementalWheel,
    OptimizedWheelChain,
)


class MarkTwo(SingleProcessorMark):
    """A virtual implementation of the MARK II enemy message encoding machine.

    Args:
        wheel1_value: The initial setting of the first wheel.
        wheel2_value: The initial setting of the second wheel.
    """

    _wheel_chain: OptimizedWheelChain

    @validate_arguments
    def __init__(self, wheel1_value: int, wheel2_value: int) -> None:
        # Having two wheels is the same as having one bigger wheel
        wheel1 = IncrementalWheel().set_value(wheel1_value)
        wheel2 = IncrementalFactorWheel().set_value(wheel2_value).set_factor(-2)
        super().__init__(OptimizedWheelChain([wheel1, wheel2]))
