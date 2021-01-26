from copy import deepcopy
from typing import List

from hypothesis import given
from hypothesis.strategies import lists, integers
from pytest import raises

from minisculus import Encoder
from minisculus.wheel import Wheel, WheelChain
from tests.search_strategies import wheels


class TestWheelChain:
    @given(
        lists(wheels(), max_size=10),
        integers(min_value=0, max_value=len(Encoder._alphabet)),
    )
    def test_valid_sequence_of_wheels(self, wheels_list: List[Wheel], index: int):
        encoder = WheelChain(wheels_list)
        # the process of encoding causes a change in internal state, so take
        # a deep copy so that the decode can start with fresh state
        decoder = deepcopy(encoder)
        assert decoder.decode(encoder.encode(index)) == index

    @given(lists(wheels(), min_size=11))
    def test_invalid_sequence_of_wheels(self, wheels_list: List[Wheel]):
        with raises(ValueError):
            WheelChain(wheels_list)
