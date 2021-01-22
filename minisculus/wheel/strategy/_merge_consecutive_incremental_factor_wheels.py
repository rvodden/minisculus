from typing import List

from minisculus.wheel import AbstractWheel, IncrementalFactorWheel
from minisculus.wheel.strategy._abstract_strategy import AbstractStrategy


class MergeConsecutiveIncrementalFactorWheels(AbstractStrategy):
    """Combines IncrementalFactorWheelsTogether.

    A wheel which adds 5, followed by another wheel which adds 5, is the same
    as a wheel which adds 10!
    """

    @classmethod
    def optimize(cls, wheels: List[AbstractWheel]) -> List[AbstractWheel]:
        """Takes a list of wheels, and returns a shorter equivalent list.

        Args:
            wheels: the list of wheels to optimize.

        Returns:
            an equivalent list of wheels.
        """
        if len(wheels) == 1:
            # cannot optimize a single wheel any more than it already is
            return wheels

        new_wheels: List[AbstractWheel] = []

        wheel_iterator = iter(wheels)

        while wheel := next(wheel_iterator, None):
            # have we found an IncrementalFactorWheel? if not,
            # stick it on the list and bail
            if not isinstance(wheel, IncrementalFactorWheel):
                new_wheels.append(wheel)
                continue
            else:
                # great! we have an IncrementalWheel lets stick it on another list
                # and see if there are any more
                wheels_to_combine = [wheel]
                while wheel := next(wheel_iterator, None):
                    if not isinstance(wheel, IncrementalFactorWheel):
                        # there are no more - combine the ones we've got so far
                        # and stick the combination on the list along with this
                        # other kind of Wheel, then bail
                        new_wheels.append(cls._combine(wheels_to_combine))
                        new_wheels.append(wheel)
                        wheels_to_combine = None
                        break
                    else:
                        # we got another one, stick it on the list and see
                        # if there are any more
                        wheels_to_combine.append(wheel)

                # if the wheels end with consecutive IncrementalWheels then
                # then they will still need to be combined
                if wheels_to_combine:
                    new_wheels.append(cls._combine(wheels_to_combine))

        return new_wheels

    @classmethod
    def _combine(cls, wheels: List[IncrementalFactorWheel]) -> IncrementalFactorWheel:
        """Combines several ``IncrementalFactorWheels`` into a single (bigger) wheel.

        Args:
            wheels: the list of wheels to combine.

        Returns:
            a single wheel which does the same job as the original list.
        """
        if len(wheels) == 1:
            return cls._convert_to_factor_of_one(wheels[0])

        # neat little bit of recursion to smash these all together
        tail = cls._combine(wheels[:-1])
        head = wheels[-1]

        # tail is always has a factor of 1 so no need to worry about the tail factor
        if head.factor > 0:
            min_value = tail.min_value + head.min_value * head.factor
            max_value = tail.max_value + head.max_value * head.factor
        else:
            min_value = tail.min_value + head.max_value * head.factor
            max_value = tail.max_value + head.min_value * head.factor

        return IncrementalFactorWheel(
            min_value=min_value, max_value=max_value
        ).set_value(tail.value + head.value * head.factor)

    @staticmethod
    def _convert_to_factor_of_one(
        wheel: IncrementalFactorWheel,
    ) -> IncrementalFactorWheel:
        """Manipulates wheel settings so the factor is 1 without altering function.

        Args:
            wheel: the wheel to be (copied and) manipulated.

        Returns:
            a copy of the wheel with equivalent function and a factor of 1.
        """
        min_value = wheel.factor * wheel.min_value
        max_value = wheel.factor * wheel.max_value
        if min_value > max_value:
            min_value, max_value = max_value, min_value
        return IncrementalFactorWheel(min_value, max_value).set_value(
            wheel.factor * wheel.value
        )
