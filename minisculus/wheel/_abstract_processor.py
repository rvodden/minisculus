from abc import ABC, abstractmethod


class AbstractProcessor(ABC):
    """A processor takes an int and returns another int."""

    @abstractmethod
    def process(self, idx: int) -> int:
        """This is the encryption function.

        Args:
            idx: the index to be encrypted.
        """
        pass
