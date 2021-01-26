"""Virtual Implementation of the MARK I."""

from pydantic import validate_arguments

from minisculus._encoder import Encoder
from minisculus.wheel import SimpleWheel


class MarkOne(Encoder):
    """A virtual implementation of the MARK I enemy message encoding machine.

    Args:
        wheel: The initial setting of the wheel.
    """

    @validate_arguments
    def __init__(self, wheel_value: int) -> None:
        wheel = SimpleWheel().set_value(wheel_value)
        super().__init__([wheel])
