from abc import ABC

from pydantic import validate_arguments

from minisculus._abstract_mark import AbstractMark
from minisculus.wheel import AbstractProcessor


class SingleProcessorMark(AbstractMark, ABC):
    """An encapsulation of single wheel MARK functionality."""

    _processor: AbstractProcessor

    def __init__(self, processor: AbstractProcessor):
        self._processor = processor

    @validate_arguments
    def _process_value(self, idx: int) -> int:
        new_position: int = self._processor.process(idx)
        return new_position
