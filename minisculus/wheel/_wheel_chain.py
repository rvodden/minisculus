from typing import List

from pydantic import validate_arguments

from minisculus.wheel._wheel import Wheel


class WheelChain:
    """Processes indexes using a chain of wheels."""

    _wheels: List[Wheel]

    def __init__(self, wheels: List[Wheel]):
        self._validate_wheels(wheels)
        self._wheels = wheels

    @validate_arguments
    def encode(self, idx: int) -> int:
        """This is the encoding function.

        Args:
            idx: the list of index to encode.

        Returns:
            the encoded index.
        """
        idxs = [idx]
        for wheel in self._wheels:
            idxs.append(wheel.encode(idxs[-1]))

        for wheel in self._wheels:
            wheel.post_encode(idxs)
        return idxs[-1]

    @validate_arguments()
    def decode(self, idx: int) -> int:
        """This is the decoding function.

        Args:
            idx: the list of indexes to be decoded.

        Returns:
            the decoded index.
        """
        idxs = [idx]
        for wheel in self._wheels:
            idxs.append(wheel.decode(idxs[-1]))

        for wheel in self._wheels:
            wheel.post_decode(idxs)
        return idxs[-1]

    @property
    @validate_arguments
    def wheels(self) -> List[Wheel]:
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

    @staticmethod
    def _validate_wheels(wheels: List[Wheel]) -> None:
        l: int = len(wheels)
        if l > 10:
            raise ValueError(
                f"WheelChain can not have more than 10 wheels. {l} provided."
            )
