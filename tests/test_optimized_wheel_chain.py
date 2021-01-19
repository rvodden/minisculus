from typing import List

from hypothesis import given
from hypothesis.strategies import integers, lists

from minisculus.wheel import AbstractWheel, IncrementalWheel, WheelChain
from minisculus.wheel._optimized_wheel_chain import OptimizedWheelChain


class TestWheelChain:
    @given(lists(integers(min_value=0, max_value=9)), integers())
    def test_sequence_of_incremental_wheels(self, values: List[int], index: int):
        wheels: List[AbstractWheel] = []
        for value in values:
            wheels.append(IncrementalWheel().set_value(value))
        under_test = OptimizedWheelChain(wheels)
        comparison = WheelChain(wheels)
        assert under_test.process(index) == comparison.process(index)
