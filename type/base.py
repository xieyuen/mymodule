from typing import Any, Generator, Iterable, Iterator, Callable


def isInteger  (x: Any) -> bool: return isinstance(x, int)
def isFloat    (x: Any) -> bool: return isinstance(x, float)
def isComplex  (x: Any) -> bool: return isinstance(x, complex)
def isString   (x: Any) -> bool: return isinstance(x, str)
def isList     (x: Any) -> bool: return isinstance(x, list)
def isTuple    (x: Any) -> bool: return isinstance(x, tuple)
def isDict     (x: Any) -> bool: return isinstance(x, dict)
def isSet      (x: Any) -> bool: return isinstance(x, set)
def isCallable (x: Any) -> bool: return isinstance(x, Callable)
def isIterable (x: Any) -> bool: return isinstance(x, Iterable)
def isIterator (x: Any) -> bool: return isinstance(x, Iterator)
def isGenerater(x: Any) -> bool: return isinstance(x, Generator)
def isBool     (x: Any) -> bool: return (x is True) or (x is False)
def isNone     (x: Any) -> bool: return x is None
