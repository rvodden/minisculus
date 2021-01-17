"""Virtual Implementation of the MARK I."""

from pydantic import validate_arguments

from minisculus._abstract_mark import AbstractMark


class MarkOne(AbstractMark):
    """A virtual implementation of the MARK I enemy message encoding machine.

    Args:
        wheel: The initial setting of the wheel.
    """

    _max_wheel_value: int
    _min_wheel_value: int

    _wheel: int

    def __init__(
        self, wheel: int, min_wheel_value: int = 0, max_wheel_value: int = 9
    ) -> None:
        self._min_wheel_value = min_wheel_value
        self._max_wheel_value = max_wheel_value
        self.wheel = wheel

    @property
    def wheel(self) -> int:
        """Gets the value of the wheel.

        Returns:
            the value of the wheel.
        """
        return self._wheel

    @wheel.setter
    @validate_arguments
    def wheel(self, value: int) -> None:
        """Sets the value of the wheel.

        Args:
            value: the value to set the wheel to.
        """
        self._validate_wheel_setting(value)
        self._wheel = value

    @validate_arguments
    def encode(self, value: str):
        """Encodes a provided single character.

        Args:
            value: the character to encode

        Returns:
            another character which is the encoded equivalent of the original
            character
        """
        self._validate_single_character(value)
        # find the position of the character in the alphabet
        position: int = self._alphabet.index(value)

        # increment this position by the value of the wheel, looping around
        # to the start if the number is bigger than the number of characters
        new_position: int = (position + self._wheel) % len(self._alphabet)

        # return the character at the new position
        return self._alphabet[new_position]

    def _validate_wheel_setting(self, value: int) -> None:
        if not self._min_wheel_value <= value <= self._max_wheel_value:
            raise ValueError(
                f"Initial wheel setting must be between {self._min_wheel_value}"
                f" and {self._max_wheel_value}. {value} was provided."
            )
