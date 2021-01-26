from hypothesis.strategies import integers

from minisculus import Encoder, MarkFour
from tests.test_encoder import TestEncoder


class TestMarkFour(TestEncoder):
    @staticmethod
    def build_encoder(draw) -> Encoder:
        wheel1_value = draw(integers(min_value=0, max_value=9))
        wheel2_value = draw(integers(min_value=0, max_value=9))
        return MarkFour(wheel1_value, wheel2_value)
