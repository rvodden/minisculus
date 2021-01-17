from hypothesis import assume, given
from hypothesis.strategies import integers, text
from pytest import raises

from minisculus import MarkOne


def _wheels():
    return integers(min_value=0, max_value=9)


class TestMarkOne:
    def test_example(self):
        """This tests the example in the text.

        The MARK I functions by shifting the input character by the number shown on the
        wheel. Therefore, with a wheel setting of 5, an input character of 'a' will result
        in an encoded character of 'f', 'c' becomes 'h', and so forth. If the new index
        falls off the end of the set of characters, then it simply loops back to the
        beginning (and vice versa).
        """
        under_test = MarkOne(5)

        assert under_test.encode("a") == "f"
        assert under_test.encode("c") == "h"

    @given(_wheels())
    def test_valid_wheel_settings(self, value):
        """Run the constructor, and assert that the value of the wheel is correct."""
        under_test: MarkOne = MarkOne(value)
        assert under_test.wheel == value

    @given(integers())
    def test_invalid_wheel_settings(self, value):
        assume(not 0 <= value <= 9)  # don't run on valid values
        with raises(ValueError):
            MarkOne(value)

    @given(_wheels(), text(alphabet=MarkOne._alphabet, min_size=2))
    def test_encode_throws_exception_when_string_is_too_long(
        self, wheel: int, string: str
    ):
        under_test: MarkOne = MarkOne(wheel)
        with raises(ValueError):
            under_test.encode(string)

    @given(_wheels(), text(alphabet=MarkOne._alphabet, min_size=1, max_size=1))
    def test_encode_returns_character_which_decodes_correctly(
        self, wheel: int, string: str
    ):
        under_test: MarkOne = MarkOne(wheel)
        encoded_value: str = under_test.encode(string)
        assert string == TestMarkOne._decode(wheel, encoded_value)

    @given(_wheels(), text(alphabet=MarkOne._alphabet))
    def test_encode_string_returns_string_which_decodes_correctly(
        self, wheel: int, string: str
    ):
        under_test: MarkOne = MarkOne(wheel)
        encoded_value: str = under_test.encode_string(string)
        assert string == TestMarkOne._decode_string(wheel, encoded_value)

    @staticmethod
    def _decode(wheel: int, value: str):
        """Reverse implementation of encode for testing"""
        if not len(value) == 1:
            raise ValueError(
                "Only single characters can be provided. A string of length"
                f"{len(value)}: {value} was provided."
            )

        # find the position of the character in the alphabet
        position: int = MarkOne._alphabet.index(value)

        # decrement this position by the value of the wheel, looping around
        # to the start if the number is bigger than the number of characters
        new_position: int = (position - wheel) % len(MarkOne._alphabet)

        # return the character at the new position
        return MarkOne._alphabet[new_position]

    @staticmethod
    def _decode_string(wheel: int, string: str):
        """Reverse implementation of encode_string for testing"""

        def decode(value: str):
            nonlocal wheel
            return TestMarkOne._decode(wheel, value)

        return "".join(list(map(decode, string)))
