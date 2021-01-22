from abc import ABC
from typing import List

from pydantic import validate_arguments


class AbstractWheel(ABC):
    """Encapsulates the common functionality of all wheels.

    A wheel is an encryption device which takes a list of numbers,
    and returns another number. It has a parameter, known
    as the ``value``, which impacts the encryption algorithm.

    This impact is unique to each implementation.

    A list is provided so that if wheels are chained together, previous
    values in the chain can influence the encryption algorithm.
    """

    _value: int
    _factor: int
    _min_value: int
    _max_value: int

    def __init__(self, min_value: int = 0, max_value: int = 9) -> None:
        if max_value < min_value:
            raise ValueError(
                f"max_value ({max_value}) must be > min_value({min_value})"
            )
        self._min_value = min_value
        self._max_value = max_value
        self._value = 0
        self._factor = 1

    @validate_arguments
    def process(self, idxs: List[int]) -> int:
        """Implements a wheel on a MARK machine.

        ADDS to the index TWO TIMES the PREVIOUS LETTER'S position in the machine's
        alphabet. Note that the third wheel's initial position starts at 0.

        Args:
            idxs: the list of indexes to encrypt

        Returns: the encrypted index
        """
        pass

    @property
    @validate_arguments
    def value(self) -> int:
        """Get the value of the wheel.

        Returns:
            the value of the wheel.
        """
        return self._value

    @value.setter
    @validate_arguments
    def value(self, value: int) -> None:
        """Set the value of the wheel.

        Args:
            value: the value to set the wheel to.
        """
        self._value = self._validate_wheel_setting(value)

    def set_value(self, value: int) -> "AbstractWheel":
        """Set the value of the wheel.

        Args:
            value: the value to set the wheel to.

        Returns:
            the wheel with the updated value.
        """
        self.value = value
        return self

    @property
    @validate_arguments
    def min_value(self) -> int:
        """Get the min_value of the wheel.

        Returns:
            the min_value of the wheel.
        """
        return self._min_value

    @property
    @validate_arguments
    def max_value(self) -> int:
        """Get the max_value of the wheel.

        Returns:
            the max_value of the wheel.
        """
        return self._max_value

    @validate_arguments
    def _validate_wheel_setting(self, value: int) -> int:
        if not self._min_value <= value <= self._max_value:
            raise ValueError(
                f"Initial wheel setting must be between {self._min_value}"
                f" and {self._max_value}. {value} was provided."
            )
        return value

    @property
    @validate_arguments
    def factor(self) -> int:
        """Get the factor of the wheel.

        Returns:
            the factor of the wheel.
        """
        return self._factor

    @factor.setter
    @validate_arguments
    def factor(self, factor: int):
        if factor == 0:
            raise ValueError("`factor` cannot be zero.")
        self._factor = factor

    def set_factor(self, factor: int) -> "AbstractWheel":
        """Fluent call to set the factor.

        Args:
            factor: the value to set the wheel factor to.

        Returns:
            the wheel with the factor set.
        """
        self.factor = factor
        return self
