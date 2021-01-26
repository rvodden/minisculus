from itertools import product
from typing import List, Tuple

from minisculus._mark_four import MarkFour


class BruteForce:
    """Used to reverse engineer the settings of a MARK IV machine."""

    @staticmethod
    def brute_force(
        message: str, clues: List[str]
    ) -> Tuple[List[Tuple[int, int]], str]:
        """Searches for MARK IV setting to decrypt a message.

        Args:
            message: the message to decode.
            clues: a list of strings which are known to be in the decoded message.

        Returns:
            the list of wheels settings which work, and the decoded message.
        """
        settings = []
        solution = None
        for i, j in product(range(10), repeat=2):
            mark = MarkFour(i, j)
            decoded = mark.decode(message)
            solved = True
            for clue in clues:
                if decoded.find(clue) < 0:
                    solved = False
                    continue
            if solved:
                solution = decoded
                settings.append((i, j))
        return settings, solution
