from abc import ABC, abstractmethod
from typing import List

from minisculus.wheel import AbstractWheel


class AbstractStrategy(ABC):
    """A way of combining multiple wheels into fewer wheels with the same function."""

    @classmethod
    @abstractmethod
    def optimize(cls, wheels: List[AbstractWheel]) -> List[AbstractWheel]:
        """Takes a list of wheels, and returns a shorter equivalent list.

        Args:
            wheels: the wheels to be optimized.
        """
        pass
