from typing import Any

from .base import isInteger, isFloat, isComplex, isBool, isIterable, isIterator
from ..mathEx.long_real import LongReal
from ..mathEx.real_num import Real


def isLongReal (x: Any) -> bool: return isinstance(x, LongReal)
def isReal     (x: Any) -> bool: return isInteger(x) or isFloat(x) or isLongReal(x) or isinstance(x, Real)
def isNumber   (x: Any) -> bool: return isComplex(x) or isReal(x)
def isEmpty    (x: Any) -> bool: return (not x) if not (isNumber(x) or isBool(x)) else False
def isNumNoBool(x: Any) -> bool: return isNumber(x) and not isBool(x)
def isCanFor   (x: Any) -> bool: return isIterable(x)
