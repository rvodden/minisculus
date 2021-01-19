from hypothesis import assume, given
from hypothesis.strategies import data, integers
from pytest import raises

from minisculus.wheel import AbstractWheel, IncrementalWheel


class TestIncrementalWheel:
    def unprocess(self, idx: int, value: int) -> int:
        return idx - value

    @given(integers(), integers(), integers())
    def test_wheel_settings(self, min_value: int, max_value: int, value: int):
        assume(min_value < max_value)
        under_test = IncrementalWheel(min_value=min_value, max_value=max_value)
        if min_value <= value <= max_value:
            under_test.value = value
            assert under_test.value == value
        else:
            with raises(ValueError):
                under_test.value = value

    @given(integers(), integers(), integers(), data())
    def test_process_returns_value_which_unprocesses_correctly(
        self, min_value: int, max_value: int, idx: int, data  # what type is this?
    ):
        assume(min_value < max_value)
        under_test: AbstractWheel = IncrementalWheel(min_value, max_value)
        # grab a valid wheel value
        value = data.draw(integers(min_value=min_value, max_value=max_value))
        under_test.value = value
        assert idx == self.unprocess(under_test.process(idx), value)
