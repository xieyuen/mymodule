from types import FunctionType, BuiltinFunctionType, MethodType, UnionType
from typing import Callable, Union

Function = Callable | FunctionType | BuiltinFunctionType | MethodType

del FunctionType, BuiltinFunctionType, MethodType, Callable


class _UnionGenericAlias:
    pass


_UnionGenericAlias = Union[_UnionGenericAlias, _UnionGenericAlias]
Types = type | UnionType | _UnionGenericAlias

__all__ = [i for i in globals() if not i.startswith("_")]
