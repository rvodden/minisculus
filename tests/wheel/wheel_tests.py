from abc import ABC, abstractmethod

from hypothesis import given
from hypothesis.strategies import data, integers, DataObject
from pytest import raises

from minisculus import Encoder
from minisculus.wheel import Wheel


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

    @given(
        integers(min_value=-9, max_value=9).filter(lambda x: x != 0),
        integers(min_value=0, max_value=len(Encoder._alphabet)),
        data(),
    )
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

    @given(integers(min_value=0, max_value=69), data())
    def test_encode_valid_character(self, index: int, data: DataObject):
        under_test = self.build_wheel(data.draw)
        assert under_test.encode(index) == index + under_test.value * under_test.factor

    @given(integers(min_value=0, max_value=69), data())
    def test_decode_valid_character(self, index: int, data: DataObject):
        under_test = self.build_wheel(data.draw)
        assert under_test.encode(index) == index - under_test.value * under_test.factor
