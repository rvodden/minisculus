from hypothesis.strategies import integers

from minisculus import MarkTwo, Encoder
from tests.test_encoder import TestEncoder


def _wheels():
    return integers(min_value=0, max_value=9)


class TestMarkTwo(TestEncoder):
    @staticmethod
    def build_encoder(draw) -> Encoder:
        wheel1_value = draw(integers(min_value=0, max_value=9))
        wheel2_value = draw(integers(min_value=0, max_value=9))
        return MarkTwo(wheel1_value, wheel2_value)

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

        assert under_test.encode("abc") == "STU"
