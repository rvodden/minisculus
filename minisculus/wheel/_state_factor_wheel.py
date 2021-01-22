from typing import List

from pydantic import validate_arguments

from minisculus.wheel import AbstractWheel


class StateFactorWheel(AbstractWheel):
    """Implementation of the MARK IV's third wheel.

    The MARK IV's third wheel is more complicated than the first two in
    that it's setting is based off the previously pressed character position.
    The machine shifts the letter based off the first two wheels,
    then it further ADDS to the index TWO TIMES the PREVIOUS LETTER'S position in the
    machine's alphabet. Note that the third wheel's initial position starts at 0.
    """

    @validate_arguments
    def process(self, idxs: List[int]) -> int:
        """Process the list of indexes.

        Args:
            idxs: the list of indexes to process

        Returns:
            the processed index
        """
        new_idx = idxs[-1] + self.value * self.factor
        # The original letter is available at idxs[0] so we set this ready for the next
        # encryption.
        #
        # We need the value to be between `min_value` and `max_value`
        # if min_value == 0 we can simply use arithmetic modulo `max_value`,
        # however if min_value is not zero that approach will mean
        # that we either ignore potential negative values (if `min_value` < 0)
        # or that we try and set invalid +ve values which are < min_value (if
        # `min_value` > 0).
        #
        # Instead we must use arithmetic modulo the difference between min_value
        # max_value (i.e. the size of the wheel). This will give us the zero
        # indexed position on the wheel we should move to. We then add that value
        # to `min_value` to give us the actual value at that position. This works for
        # `min_value` == 0 too (as `max_value` - 0 == `max_value`) hence the below.
        #
        self.value = (idxs[0] % (self.max_value - self.min_value)) + self.min_value
        return new_idx
