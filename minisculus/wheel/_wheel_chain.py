from typing import List

from minisculus.wheel._abstract_processor import AbstractProcessor
from minisculus.wheel._abstract_wheel import AbstractWheel


class WheelChain(AbstractProcessor):
    """Processes indexes using a chain of wheels."""

    _wheels: List[AbstractWheel]

    def __init__(self, wheels: List[AbstractWheel]):
        self._wheels = wheels

    def process(self, idx: int) -> int:
        """This is the encryption function.

        Args:
            idx: the index to be encrypted.

        Returns:
            the encrypted index.
        """
        new_idx = idx
        for wheel in self._wheels:
            new_idx = wheel.process(new_idx)
        return new_idx

    @property
    def wheels(self) -> List[AbstractWheel]:
        """Returns the wheels which constitutes the WheelChain.

        Returns:
            list of wheels.
        """
        return self._wheels

    @property
    def values(self) -> List[int]:
        """Returns a list of the values of each of the wheels.

        Returns:
            list of wheels.
        """
        return [w.value for w in self._wheels]
