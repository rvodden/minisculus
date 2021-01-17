from hypothesis import assume, given
from hypothesis.strategies import integers, text
from pytest import raises

from minisculus import MarkTwo


def _wheels():
    return integers(min_value=0, max_value=9)


class TestMarkTwo:
    def test_example(self):
        """This tests the example in the text.

        The MARK II has a design evolved from the MARK I in that it still has a letter
        shifting first wheel, however, a second wheel has been added to further
        complicate the encoded message. The MARK II's second wheel is set the same way
        as the first, e.g. a 0-9 setting. The difference is that the second wheel shifts
        the characters in a REVERSE direction TWO TIMES the number shown on the wheel's
        setting. This means, a MARK II machine with wheel settings of 2 [First Wheel],
        5 [Second Wheel] and input characters of 'abc' will result in an output of 'STU'
        """
        under_test = MarkTwo(2, 5)

        assert under_test.encode_string("abc") == "STU"

    @given(_wheels(), _wheels())
    def test_valid_wheel_settings(self, wheel_one, wheel_two):
        """Run the constructor, and assert that the value of the wheel is correct."""
        under_test: MarkTwo = MarkTwo(wheel_one, wheel_two)
        assert under_test.wheel_one == wheel_one
        assert under_test.wheel_two == wheel_two

    @given(integers(), integers())
    def test_invalid_wheel_settings(self, wheel_one, wheel_two):
        # at least one wheel must be invalid
        assume(not 0 <= wheel_one <= 9 or not 0 <= wheel_two <= 9)

        with raises(ValueError):
            MarkTwo(wheel_one, wheel_two)

    @given(_wheels(), _wheels(), text(alphabet=MarkTwo._alphabet, min_size=2))
    def test_encode_throws_exception_when_string_is_too_long(
        self, wheel_one: int, wheel_two: int, string: str
    ):
        under_test: MarkTwo = MarkTwo(wheel_one, wheel_two)
        with raises(ValueError):
            under_test.encode(string)

    @given(
        _wheels(), _wheels(), text(alphabet=MarkTwo._alphabet, min_size=1, max_size=1)
    )
    def test_encode_returns_character_which_decodes_correctly(
        self, wheel_one: int, wheel_two: int, string: str
    ):
        under_test: MarkTwo = MarkTwo(wheel_one, wheel_two)
        encoded_value: str = under_test.encode(string)
        assert string == TestMarkTwo._decode(wheel_one, wheel_two, encoded_value)

    @given(_wheels(), _wheels(), text(alphabet=MarkTwo._alphabet))
    def test_encode_string_returns_string_which_decodes_correctly(
        self, wheel_one: int, wheel_two: int, string: str
    ):
        under_test: MarkTwo = MarkTwo(wheel_one, wheel_two)
        encoded_value: str = under_test.encode_string(string)
        assert string == self._decode_string(wheel_one, wheel_two, encoded_value)

    @staticmethod
    def _decode(wheel_one: int, wheel_two: int, value: str):
        """Reverse implementation of encode for testing"""
        if not len(value) == 1:
            raise ValueError(
                "Only single characters can be provided. A string of length"
                f"{len(value)}: {value} was provided."
            )

        # find the position of the character in the alphabet
        position: int = MarkTwo._alphabet.index(value)

        # decrement this position by the value of the wheel, looping around
        # to the start if the number is bigger than the number of characters
        new_position: int = (position - wheel_one + 2 * wheel_two) % len(
            MarkTwo._alphabet
        )

        # return the character at the new position
        return MarkTwo._alphabet[new_position]

    @classmethod
    def _decode_string(cls, wheel_one: int, wheel_two: int, string: str):
        """Reverse implementation of encode_string for testing"""

        def decode(value: str):
            nonlocal wheel_one, wheel_two
            return cls._decode(wheel_one, wheel_two, value)

        return "".join(list(map(decode, string)))
