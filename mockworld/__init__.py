"""Mock UK lettings world: data, stateful World, and the MockAdapter.

Used as test fixtures before the event and as the `make demo` environment
when the organisers' data cannot be redistributed.
"""

from .adapter import MockAdapter
from .world import World

__all__ = ["MockAdapter", "World"]
