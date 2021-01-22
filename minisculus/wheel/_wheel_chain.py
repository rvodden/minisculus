from typing import List

from pydantic import validate_arguments

from minisculus.wheel._abstract_wheel import AbstractWheel


class WheelChain:
    """Processes indexes using a chain of wheels."""

    _wheels: List[AbstractWheel]

    def __init__(self, wheels: List[AbstractWheel]):
        self._wheels = wheels

    @validate_arguments
    def process(self, idxs: List[int]) -> int:
        """This is the encryption function.

        Args:
            idxs: the list of indexes to be encrypted.

        Returns:
            the encrypted index.
        """
        for wheel in self._wheels:
            idxs.append(wheel.process(idxs))
        return idxs[-1]

    @property
    @validate_arguments
    def wheels(self) -> List[AbstractWheel]:
        """Returns the wheels which constitutes the WheelChain.

        Returns:
            list of wheels.
        """
        return self._wheels

    @property
    @validate_arguments
    def values(self) -> List[int]:
        """Returns a list of the values of each of the wheels.

        Returns:
            list of wheels.
        """
        return [w.value for w in self._wheels]
