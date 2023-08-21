from typing import Any

from .base import isInteger, isString, isDict
from .extra import isNumber, isCharacter


def isInt(x: Any) -> bool: return isInteger(x)
def isStr(x: Any) -> bool: return isString(x)
def isDictionary(x: Any) -> bool: return isDict(x)
def isNum(x: Any) -> bool: return isNumber(x)
def isChar(x: Any) -> bool: return isCharacter(x)