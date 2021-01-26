from pydantic import validate_arguments

from minisculus.wheel._wheel import Wheel


class SimpleWheel(Wheel):
    """A wheel which functions by incrementing the index by value * factor."""

    @validate_arguments
    def _encode(self, idx: int) -> int:
        return idx + self.value * self.factor

    @validate_arguments
    def _decode(self, idx: int) -> int:
        return idx - self.value * self.factor

    def __repr__(self) -> str:
        """A representation of the wheel.

        Returns:
            the string representation of the wheel.
        """
        return (
            f"SimpleWheel({self.min_value, self.max_value})"
            f"[{self.factor}, {self.value}]"
        )
