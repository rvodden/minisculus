from pydantic import validate_arguments

from minisculus import MarkOne
from minisculus._abstract_mark import AbstractMark


class MarkTwo(AbstractMark):
    """A virtual implementation of the MARK II enemy message encoding machine.

    Args:
        wheel_one: The initial setting of the first wheel.
        wheel_two: The initial setting of the second wheel.
    """

    _min_wheel_value: int
    _max_wheel_value: int

    _mark_one: MarkOne = None
    _wheel_one: int = 0
    _wheel_two: int = 0

    @validate_arguments
    def __init__(
        self,
        wheel_one: int,
        wheel_two: int,
        min_wheel_value: int = 0,
        max_wheel_value: int = 9,
    ) -> None:
        # having a mark one with two wheels, is the same as having a
        # mark one with a bigger wheel which goes from -18 to 9
        self._min_wheel_value = min_wheel_value
        self._max_wheel_value = max_wheel_value
        self.wheel_one = wheel_one
        self.wheel_two = wheel_two
        min_m1_wheel_value = self._calculate_wheel_value(
            min_wheel_value, max_wheel_value
        )
        max_m1_wheel_value = self._calculate_wheel_value(
            max_wheel_value, min_wheel_value
        )
        self._mark_one = MarkOne(
            self._calculate_wheel_value(wheel_one, wheel_two),
            min_wheel_value=min_m1_wheel_value,
            max_wheel_value=max_m1_wheel_value,
        )

    @property
    def wheel_one(self) -> int:
        """Gets the value of wheel one.

        Returns:
            the value of the wheel.
        """
        return self._wheel_one

    @wheel_one.setter
    def wheel_one(self, value: int) -> None:
        """Sets the value of wheel one.

        Args:
            value: the value to set wheel one to.
        """
        self._validate_wheel_value(value)
        self._wheel_one = value
        self._set_wheel()

    @property
    def wheel_two(self) -> int:
        """Gets the value of wheel two.

        Returns:
            the value of the wheel.
        """
        return self._wheel_two

    @wheel_two.setter
    def wheel_two(self, value: int) -> None:
        """Sets the value of wheel two.

        Args:
            value: the value to set wheel two to.
        """
        self._validate_wheel_value(value)
        self._wheel_two = value
        self._set_wheel()

    def _set_wheel(self) -> None:
        if self._mark_one:
            self._mark_one.wheel = self._calculate_wheel_value(
                self.wheel_one, self.wheel_two
            )

    @staticmethod
    @validate_arguments()
    def _calculate_wheel_value(wheel_one: int, wheel_two: int) -> int:
        return wheel_one - 2 * wheel_two

    @validate_arguments()
    def _validate_wheel_value(self, value: int) -> None:
        if not self._min_wheel_value <= value <= self._max_wheel_value:
            raise ValueError(
                f"Initial wheel setting must be between "
                f"{self._min_wheel_value}"
                f" and {self._max_wheel_value}. {value} was provided."
            )

    @validate_arguments
    def encode(self, value: str) -> str:
        """Encodes a provided single character.

        Args:
            value: the character to encode

        Returns:
            another character which is the encoded equivalent of the original
            character
        """
        return self._mark_one.encode(value)
