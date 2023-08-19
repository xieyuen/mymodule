from typing import Any

from .base import isInteger, isString
from .extra import isNumber


def isInt(x: Any) -> bool: return isInteger(x)
def isStr(x: Any) -> bool: return isString(x)
def isNum(x: Any) -> bool: return isNumber(x)
