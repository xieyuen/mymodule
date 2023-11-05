from numbers import Number, Real
from types import FunctionType, MethodType, BuiltinMethodType, BuiltinFunctionType
from typing import Any, Iterable, Container, Hashable

from .base import isStr, isBool, isIterable
from .new_type import Array
from ..math_ex.long_real import LongReal

__all__ = [
    'isLongReal', 'isReal', 'isNumber', 'isEmpty',
    'isNumNoBool', 'isCanFor', 'isImmutable', 'isDouble',
    'isCharacter', 'isArray', 'isFunction', 'isMethod',
    'isBuiltin',
]


def isLongReal(x: Any) -> bool: return isinstance(x, LongReal)


def isReal(x: Any) -> bool: return isinstance(x, Real) or isLongReal(x)


def isNumber(x: Any) -> bool: return isinstance(x, Number) or isLongReal(x)


def isEmpty(x: Any) -> bool: return len(x) == 0


def isContainer(x: Any) -> bool: return isinstance(x, Container)


def isNumNoBool(x: Any) -> bool: return isNumber(x) and not isBool(x)


def isCanFor(x: Any) -> bool: return isIterable(x)


def isCharacter(x: Any) -> bool: return len(x) == 1 if isStr(x) else False


def isMethod(x: Any) -> bool: return isinstance(x, MethodType) or isinstance(x, BuiltinMethodType)


def isFunction(x: Any) -> bool: return isinstance(x, FunctionType) or isinstance(x, BuiltinFunctionType) or isMethod(x)


def isBuiltin(x: Any) -> bool: return x.__module__ == 'builtins'


def isDouble(x: Any) -> exit:
    raise TypeError("Python 不支持 Double 类型 | Double types is not supported in Python")


def isArray(x: Iterable) -> bool:
    if not isinstance(x, list):
        return False
    if isinstance(x, Array):
        return True
    __type = type(x[0])
    for t in [type(i) for i in x]:
        if t != __type:
            return False
    return True


def isImmutable(x: Any) -> bool:
    try:
        dict()[x] = 1
        return True
    except TypeError:
        return False


def isHashable(x: Any) -> bool: return isinstance(x, Hashable)
