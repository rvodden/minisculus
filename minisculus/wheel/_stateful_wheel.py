from typing import List

from pydantic import validate_arguments

from minisculus.wheel import SimpleWheel


class StatefulWheel(SimpleWheel):
    """Implementation of the MARK IV's third wheel.

    The MARK IV's third wheel is more complicated than the first two in
    that it's setting is based off the previously pressed character position.
    The machine shifts the letter based off the first two wheels,
    then it further ADDS to the index TWO TIMES the PREVIOUS LETTER'S position in the
    machine's alphabet. Note that the third wheel's initial position starts at 0.
    """

    def __init__(self) -> None:
        # TODO: should not have the length of the alphabet hardcoded here.
        super().__init__(0, 69)

    @validate_arguments
    def post_encode(self, idxs: List[int]) -> None:
        """Set the wheel to the original character.

        Args:
            idxs: a list of indexes.
        """
        self.value = idxs[0]

    @validate_arguments
    def post_decode(self, idxs: List[int]) -> None:
        """Set the wheel to the decoded character.

        Args:
            idxs: a list of indexes.
        """
        # TODO: length of alphabet shouldn't be hardcoded here
        self.value = idxs[-1] % self.max_value

    def __repr__(self) -> str:
        """A representation of the wheel.

        Returns:
            the string representation of the wheel.
        """
        return (
            f"StatefulWheel({self.min_value, self.max_value})"
            f"[{self.factor}{self.value}]"
        )
