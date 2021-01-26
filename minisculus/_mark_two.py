from pydantic import validate_arguments

from minisculus._encoder import Encoder
from minisculus.wheel import SimpleWheel


class MarkTwo(Encoder):
    """A virtual implementation of the MARK II enemy message encoding machine.

    Args:
        wheel1_value: The initial setting of the first wheel.
        wheel2_value: The initial setting of the second wheel.
    """

    @validate_arguments
    def __init__(self, wheel1_value: int, wheel2_value: int) -> None:
        # Having two wheels is the same as having one bigger wheel
        wheel1 = SimpleWheel().set_value(wheel1_value)
        wheel2 = SimpleWheel().set_value(wheel2_value).set_factor(-2)
        super().__init__([wheel1, wheel2])
