from hypothesis.strategies import integers

from minisculus.wheel import Wheel, SimpleWheel
from tests.wheel.wheel_tests import WheelTests


class TestSimpleWheel(WheelTests):
    def build_wheel(self, draw) -> Wheel:
        min_value = draw(integers())
        max_value = draw(integers(min_value=min_value + 1))
        return SimpleWheel(min_value=min_value, max_value=max_value)
