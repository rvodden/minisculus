from pydantic import validate_arguments

from minisculus._abstract_mark import AbstractMark
from minisculus.wheel import IncrementalFactorWheel, StateFactorWheel


class MarkFour(AbstractMark):
    """The MARKIV is based on the MARKII and has three wheels.

    The MARK IV's third wheel is more complicated than the first two in that it's
    setting is based off the previously pressed character position. The machine shifts
    the letter based off the first two wheels, then it further ADDS to the index
    TWO TIMES the PREVIOUS LETTER'S position in the machine's alphabet.

    Note that the third wheel's initial position starts at 0.
    """

    @validate_arguments
    def __init__(self, wheel1_value: int, wheel2_value: int) -> None:
        wheel1 = IncrementalFactorWheel().set_value(wheel1_value)
        wheel2 = IncrementalFactorWheel().set_value(wheel2_value).set_factor(-2)
        wheel3 = StateFactorWheel(0, len(self._alphabet)).set_value(0).set_factor(2)
        super().__init__([wheel1, wheel2, wheel3])
