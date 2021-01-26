from pydantic import validate_arguments

from minisculus._encoder import Encoder
from minisculus.wheel import SimpleWheel, StatefulWheel


class MarkFour(Encoder):
    """The MARKIV is based on the MARKII and has three wheels.

    The MARK IV's third wheel is more complicated than the first two in that it's
    setting is based off the previously pressed character position. The machine shifts
    the letter based off the first two wheels, then it further ADDS to the index
    TWO TIMES the PREVIOUS LETTER'S position in the machine's alphabet.

    Note that the third wheel's initial position starts at 0.
    """

    @validate_arguments
    def __init__(self, wheel1_value: int, wheel2_value: int) -> None:
        wheel1 = SimpleWheel().set_value(wheel1_value)
        wheel2 = SimpleWheel().set_value(wheel2_value).set_factor(-2)
        wheel3 = StatefulWheel().set_factor(2)
        super().__init__([wheel1, wheel2, wheel3])
