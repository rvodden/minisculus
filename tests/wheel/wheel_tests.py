from abc import ABC, abstractmethod

from hypothesis import given
from hypothesis.strategies import data, integers, DataObject
from pytest import raises

from minisculus.wheel import Wheel
from tests.search_strategies import valid_indexes, valid_factors


class WheelTests(ABC):
    @abstractmethod
    def build_wheel(self, draw):
        pass

    @given(integers(), integers(), data())
    def test_wheel_settings(self, factor: int, value: int, data):
        under_test = self.build_wheel(data.draw)
        if under_test.min_value <= value <= under_test.max_value:
            under_test.set_value(value)
            assert under_test.value == value
        else:
            with raises(ValueError):
                under_test.set_value(value)

        if factor != 0 and -10 < factor < 10:
            under_test.set_factor(factor)
            assert under_test.factor == factor
        else:
            with raises(ValueError):
                under_test.set_factor(factor)

    @given(valid_factors(), valid_indexes(), data())
    def test_process_returns_value_which_unprocesses_correctly(
        self, factor: int, idx: int, data
    ):
        under_test: Wheel = self.build_wheel(data.draw)
        value = data.draw(
            integers(min_value=under_test.min_value, max_value=under_test.max_value),
            label="value",
        )

        under_test.factor = factor
        under_test.value = value

        # grab a valid wheel value
        assert idx == under_test.decode(under_test.encode(idx))

    @given(valid_indexes(), data())
    def test_encode_valid_character(self, index: int, data: DataObject):
        under_test = self.build_wheel(data.draw)
        assert under_test.encode(index) == index + under_test.value * under_test.factor

    @given(valid_indexes(), data())
    def test_decode_valid_character(self, index: int, data: DataObject):
        under_test = self.build_wheel(data.draw)
        assert under_test.encode(index) == index - under_test.value * under_test.factor
