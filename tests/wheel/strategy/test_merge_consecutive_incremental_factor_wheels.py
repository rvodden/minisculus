from hypothesis import given
from hypothesis.strategies import data, integers, lists

from minisculus.wheel import IncrementalWheel, WheelChain
from minisculus.wheel.strategy import MergeConsecutiveIncrementalFactorWheels


class TestMergeConsecutiveIncrementalFactorWheels:
    @given(lists(integers(min_value=0, max_value=9), min_size=1), integers())
    def test_combine_with_consuctive_factor_wheels(self, values, index):
        wheels = []
        for value in values:
            wheels.append(IncrementalWheel().set_value(value))
        wheel_chain = WheelChain(wheels)
        under_test = WheelChain(
            MergeConsecutiveIncrementalFactorWheels.optimize(wheels)
        )

        # this wheel chain only has IncrementalWheels in it, so it should smash
        # down to a single wheel
        assert len(under_test.wheels) == 1

        # check that the optimized WHeelChain does what the original does
        assert wheel_chain.process(index) == under_test.process(index)

    @given(lists(integers().filter(lambda x: x != 0), min_size=1), integers(), data())
    def test_combine_with_consecutive_incremental_wheels(self, factors, index, data):
        wheels = []
        for factor in factors:
            value = data.draw(integers(min_value=0, max_value=9))
            wheels.append(IncrementalWheel().set_value(value).set_factor(factor))
        wheel_chain = WheelChain(wheels)
        under_test = WheelChain(
            MergeConsecutiveIncrementalFactorWheels.optimize(wheels)
        )

        # this wheel chain only has IncrementalWheels in it, so it should smash
        # down to a single wheel
        assert len(under_test.wheels) == 1

        # check that the optimized WHeelChain does what the original does
        assert wheel_chain.process(index) == under_test.process(index)
