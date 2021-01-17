"""Virtual Implementation of the MARK I."""

from typing import List

from pydantic import validate_arguments


class MarkOne:
    """A virtual implementation of the MARK I enemy message encoding machine.

    Args:
        wheel: The initial setting of the wheel.
    """

    _MAX_WHEEL_VALUE = 9
    _MIN_WHEEL_VALUE = 0

    _wheel: int
    _alphabet: List[str] = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        ".",
        ",",
        "?",
        "!",
        "'",
        '"',
        " ",
    ]

    def __init__(self, wheel: int) -> None:
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

        Raises:
            ValueError: if the wheel value is out of range.
        """
        if not self._MIN_WHEEL_VALUE <= value <= self._MAX_WHEEL_VALUE:
            raise ValueError(
                f"Initial wheel setting must be between {self._MIN_WHEEL_VALUE}"
                f" and {self._MIN_WHEEL_VALUE}. f{value} was provided."
            )
        self._wheel = value

    @validate_arguments
    def encode(self, value: str):
        """Encodes a provided single character.

        Args:
            value: the character to encode

        Returns:
            another character which is the encoded equivalent of the original
            character

        Raises:
            ValueError: if more than a single character is provided
        """
        if not len(value) == 1:
            raise ValueError(
                "Only single characters can be provided. A string of length"
                f"{len(value)}: {value} was provided."
            )

        # find the position of the character in the alphabet
        position: int = self._alphabet.index(value)

        # increment this position by the value of the wheel, looping around
        # to the start if the number is bigger than the number of characters
        new_position: int = (position + self._wheel) % len(self._alphabet)

        # return the character at the new position
        return self._alphabet[new_position]

    @validate_arguments
    def encode_string(self, string: str):
        """Encodes a string.

        Args:
            string: the string to encode.

        Returns:
            A new string with each character in turn encoded.

        """
        return "".join(list(map(self.encode, string)))
