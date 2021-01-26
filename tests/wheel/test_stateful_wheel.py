from hypothesis import given
from hypothesis.strategies import data, DataObject

from minisculus.wheel import StatefulWheel
from tests.wheel.wheel_tests import WheelTests


class TestStatefulWheel(WheelTests):
    def build_wheel(self, draw):
        return StatefulWheel()

    @given(data())
    def test_initial_value_is_zero(self, data: DataObject):
        under_test = self.build_wheel(data.draw)
        assert under_test.value == 0
