from hypothesis import given, assume
from hypothesis.strategies import data, integers
from pytest import raises

from minisculus.wheel import StateFactorWheel, AbstractWheel


class TestStateFactorWheel:
    def unprocess(self, idx: int, factor: int, value: int) -> int:
        return idx - value * factor

    @given(integers(), integers(), integers(), integers())
    def test_wheel_settings(
        self, min_value: int, max_value: int, factor: int, value: int
    ):
        assume(min_value < max_value)
        under_test = StateFactorWheel(min_value=min_value, max_value=max_value)
        if min_value <= value <= max_value:
            under_test.set_value(value)
            assert under_test.value == value
        else:
            with raises(ValueError):
                under_test.set_value(value)

        if factor != 0:
            under_test.set_factor(factor)
            assert under_test.factor == factor
        else:
            with raises(ValueError):
                under_test.set_factor(factor)

    @given(integers(), integers(), integers(), data())
    def test_process(self, min_value: int, max_value: int, idx: int, data):
        assume(min_value < max_value)
        idx = data.draw(integers(min_value=min_value, max_value=max_value))

        under_test: AbstractWheel = StateFactorWheel(min_value, max_value)
        # grab a valid wheel value
        value = data.draw(
            integers(min_value=min_value, max_value=max_value), label="value"
        )
        factor = data.draw(integers().filter(lambda x: x != 0), label="factor")
        under_test.factor = factor
        under_test.value = value
        assert idx == self.unprocess(under_test.process([idx]), factor, value)
        assert (
            under_test.value
            == (idx % (under_test.max_value - under_test.min_value))
            + under_test.min_value
        )
