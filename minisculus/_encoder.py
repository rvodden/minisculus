from typing import Callable, List

from pydantic import validate_arguments

from minisculus.wheel import Wheel, WheelChain


class Encoder:
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

    _wheel_chain: WheelChain

    def __init__(self, wheels: List[Wheel]):
        self._wheel_chain = WheelChain(wheels)

    @validate_arguments
    def encode(self, string: str) -> str:
        """Encodes a string.

        Args:
            string: the string to encode.

        Returns:
            A new string with each character in turn encoded.

        """
        return self._run_on_each_character(self._encode_character, string)

    @validate_arguments
    def decode(self, string: str) -> str:
        """Encodes a string.

        Args:
            string: the string to encode.

        Returns:
            A new string with each character in turn encoded.

        """
        return self._run_on_each_character(self._decode_character, string)

    @validate_arguments
    def _run_on_each_character(self, process: Callable[[str], str], string: str) -> str:
        self._validate_string(string)
        if len(string) == 0:
            return string
        return "".join(list(map(process, string)))

    @validate_arguments
    def _encode_character(self, char: str) -> str:
        return self._process_character(self._encode_index, char)

    @validate_arguments
    def _decode_character(self, char: str) -> str:
        return self._process_character(self._decode_index, char)

    @validate_arguments
    def _process_character(self, process: Callable[[int], int], char: str) -> str:
        self._validate_single_character(char)
        idx: int = self._alphabet.index(char)
        new_idx: int = process(idx) % len(self._alphabet)
        return self._alphabet[new_idx]

    @staticmethod
    @validate_arguments
    def _validate_single_character(value: str) -> None:
        if not len(value) == 1:
            raise ValueError(
                "Only single characters can be provided. A string of length"
                f" {len(value)}: '{value}' was provided."
            )

    @classmethod
    @validate_arguments
    def _validate_string(cls, string: str) -> None:
        if not all(char in cls._alphabet for char in string):
            raise ValueError(
                "The string must not include characters"
                "from outside the alphabet. '{string}' provided."
            )

    @validate_arguments
    def _encode_index(self, idx: int) -> int:
        return self._wheel_chain.encode(idx)

    @validate_arguments
    def _decode_index(self, idx: int) -> int:
        return self._wheel_chain.decode(idx)

    @property
    def wheel_chain(self) -> WheelChain:
        """The wheel chain of the machine.

        Returns:
            a list of wheels.
        """
        return self._wheel_chain
