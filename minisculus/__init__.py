"""Richard Vodden's entry to the minisculus challenge."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    pass

from minisculus._mark_one import MarkOne
from minisculus._mark_two import MarkTwo
from minisculus._single_processor_mark import SingleProcessorMark

__all__ = ["MarkOne", "MarkTwo", "SingleProcessorMark"]
