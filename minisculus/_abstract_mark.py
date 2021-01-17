from abc import ABC, abstractmethod
from typing import List

from pydantic import validate_arguments


class AbstractMark(ABC):
    """A base class which abstracts the functionality of all the MARK machines."""

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

    @abstractmethod
    def encode(self, value: str) -> str:
        """Encodes a provided single character.

        Args:
            value: the character to encode
        """
        pass

    @validate_arguments
    def encode_string(self, string: str) -> str:
        """Encodes a string.

        Args:
            string: the string to encode.

        Returns:
            A new string with each character in turn encoded.

        """
        return "".join(list(map(self.encode, string)))

    @staticmethod
    def _validate_single_character(value: str) -> None:
        if not len(value) == 1:
            raise ValueError(
                "Only single characters can be provided. A string of length"
                f"{len(value)}: {value} was provided."
            )