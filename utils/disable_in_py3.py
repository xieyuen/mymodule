__all__ = [
    "cmp",
]

from numbers import Real
from typing import Literal


def cmp(x: Real, y: Real) -> Literal[-1, 0, 1]:
    return (x > y) - (x < y)
