from typing import List

from pydantic import validate_arguments

from minisculus.wheel._abstract_wheel import AbstractWheel


class IncrementalFactorWheel(AbstractWheel):
    """A wheel which functions by incrementing the index by value * factor."""

    @validate_arguments
    def process(self, idxs: List[int]) -> int:
        """This is the encryption function.

        Args:
            idxs: the indexes to be encrypted

        Returns:
            the encrypted index value.
        """
        return idxs[-1] + self.value * self.factor
