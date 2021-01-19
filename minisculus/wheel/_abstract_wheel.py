from abc import ABC

from minisculus.wheel._abstract_processor import AbstractProcessor


class AbstractWheel(AbstractProcessor, ABC):
    """Encapsulates the common functionality of all wheels.

    A wheel is an encryption device which takes a number,
    and returns another number. It has a parameter, known
    as the ``value``, which impacts the encryption algorithm.
    This impact is unique to each implementation.
    """

    _value: int
    _min_value: int
    _max_value: int

    def __init__(self, min_value: int = 0, max_value: int = 9) -> None:
        if max_value < min_value:
            raise ValueError(
                f"max_value ({max_value}) must be > min_value({min_value})"
            )
        self._min_value = min_value
        self._max_value = max_value
        self._value = None

    @property
    def value(self) -> int:
        """Get the value of the wheel.

        Returns:
            the value of the wheel.
        """
        return self._value

    @value.setter
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
    def min_value(self) -> int:
        """Get the min_value of the wheel.

        Returns:
            the min_value of the wheel.
        """
        return self._min_value

    @property
    def max_value(self) -> int:
        """Get the max_value of the wheel.

        Returns:
            the max_value of the wheel.
        """
        return self._max_value

    def _validate_wheel_setting(self, value: int) -> int:
        if not self._min_value <= value <= self._max_value:
            raise ValueError(
                f"Initial wheel setting must be between {self._min_value}"
                f" and {self._max_value}. {value} was provided."
            )
        return value
