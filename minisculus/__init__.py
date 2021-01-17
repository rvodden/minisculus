"""Richard Vodden's entry to the minisculus challenge."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    pass

from minisculus._mark_one import MarkOne
from minisculus._mark_two import MarkTwo

__all__ = ["MarkOne", "MarkTwo"]
