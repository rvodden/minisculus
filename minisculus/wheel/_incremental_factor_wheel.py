from minisculus.wheel import AbstractWheel


class IncrementalFactorWheel(AbstractWheel):
    """A wheel which functions by incrementing the character by value * factor."""

    _factor: int

    def process(self, idx: int) -> int:
        """This is the encryption function.

        Args:
            idx: the index to be encrypted

        Returns:
            the encrypted index value.
        """
        return idx + self.value * self.factor

    @property
    def factor(self) -> int:
        """Get the factor of the wheel.

        Returns:
            the factor of the wheel.
        """
        return self._factor

    @factor.setter
    def factor(self, factor: int):
        """Set the factor of the wheel.

        Args:
            factor: the value to set the wheel factor to.

        Raises:
            ValueError: when factor is zero.
        """
        if factor == 0:
            raise ValueError("`factor` cannot be zero.")
        self._factor = factor

    def set_factor(self, factor: int) -> "IncrementalFactorWheel":
        """Set the factor of the wheel.

        Args:
            factor: the value to set the wheel factor to.

        Returns:
            the wheel with the factor set.
        """
        self.factor = factor
        return self
