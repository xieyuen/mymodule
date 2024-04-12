from types import FunctionType, BuiltinFunctionType, MethodType
from typing import Callable

Function = Callable | FunctionType | BuiltinFunctionType | MethodType

del FunctionType, BuiltinFunctionType, MethodType, Callable

__all__ = [i for i in globals() if not i.startswith("_")]
