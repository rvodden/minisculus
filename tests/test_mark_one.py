from hypothesis.strategies import integers

from minisculus import MarkOne, Encoder
from tests.test_encoder import TestEncoder


class TestMarkOne(TestEncoder):
    @staticmethod
    def build_encoder(draw) -> Encoder:
        wheel1_value = draw(integers(min_value=0, max_value=9))
        return MarkOne(wheel1_value)

    def test_example(self):
        """This tests the example in the text.

        The MARK I functions by shifting the input character by the number shown on the
        wheel. Therefore, with a wheel setting of 5, an input character of 'a' will result
        in an encoded character of 'f', 'c' becomes 'h', and so forth. If the new index
        falls off the end of the set of characters, then it simply loops back to the
        beginning (and vice versa).
        """
        under_test = MarkOne(5)

        assert under_test._encode_character("a") == "f"
        assert under_test._encode_character("c") == "h"
