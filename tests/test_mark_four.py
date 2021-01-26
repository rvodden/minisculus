from minisculus import Encoder, MarkFour
from tests.search_strategies import valid_wheel_values
from tests.test_encoder import TestEncoder


class TestMarkFour(TestEncoder):
    @staticmethod
    def build_encoder(draw) -> Encoder:
        wheel1_value = draw(valid_wheel_values())
        wheel2_value = draw(valid_wheel_values())
        return MarkFour(wheel1_value, wheel2_value)
