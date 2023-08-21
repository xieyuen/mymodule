from typing import Any

from base import isInteger, isString, isDict, isBool
from extra import isNumber, isCharacter


__all__ = [
    "isInt", "isStr", "isDictionary", "isNum", "isChar",
    'isMap', 'isBoolean'
]


def isInt(x: Any) -> bool: return isInteger(x)


def isStr(x: Any) -> bool: return isString(x)


def isDictionary(x: Any) -> bool: return isDict(x)


def isNum(x: Any) -> bool: return isNumber(x)


def isChar(x: Any) -> bool: return isCharacter(x)


def isMap(x: Any) -> bool: return isDict(x)


def isBoolean(x: Any) -> bool: return isBool(x)
