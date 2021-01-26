from abc import ABC, abstractmethod
from typing import List

from pydantic import validate_arguments


class Wheel(ABC):
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
    def encode(self, idx: int) -> int:
        """Implements a wheel on a MARK machine.

        Args:
            idx: the list of indexes to encode

        Returns:
            the encoded index
        """
        return self._encode(idx)

    @abstractmethod
    def _encode(self, idx: int) -> int:
        pass

    @validate_arguments
    def decode(self, idx: int) -> int:
        """Performs the inverse action of the wheels encode function.

        Args:
            idx: the list of indexes to decode

        Returns:
            the decoded index
        """
        return self._decode(idx)

    @abstractmethod
    def _decode(self, idx: int) -> int:
        pass

    def post_encode(self, idxs: List[int]) -> None:
        """Called by the WheelChain after encoding has complete.

        Args:
            idxs: the list of indexes
        """
        pass

    def post_decode(self, idxs: List[int]) -> None:
        """Called by the WheelChain after decoding has complete.

        Args:
            idxs: the list of indexes
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
        self._value = self._validate_wheel_value(value)

    def set_value(self, value: int) -> "Wheel":
        """Set the value of the wheel.

        Args:
            value: the value to set the wheel to.

        Returns:
            the wheel with the updated value.
        """
        self.value = value
        return self

    @validate_arguments
    def _validate_wheel_value(self, value: int) -> int:
        if not self._min_value <= value <= self._max_value:
            raise ValueError(
                f"Initial wheel setting must be between {self._min_value}"
                f" and {self._max_value}. {value} was provided."
            )
        return value

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
        self._factor = self._validate_wheel_factor(factor)

    def set_factor(self, factor: int) -> "Wheel":
        """Fluent call to set the factor.

        Args:
            factor: the value to set the wheel factor to.

        Returns:
            the wheel with the factor set.
        """
        self.factor = factor
        return self

    @validate_arguments
    def _validate_wheel_factor(self, factor: int) -> int:
        if (not -10 < factor < 10) or factor == 0:
            raise ValueError(
                f"Wheel factor must be between -9"
                f" and 9 and cannot be zero. {factor} was provided."
            )
        return factor
