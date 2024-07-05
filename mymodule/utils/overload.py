__all__ = ["overload"]

from typing import Callable, Tuple

from .._utils.types import Function


class OverloadCache:
    def __init__(self):
        self.__cache = {}

    def __getitem__(self, item) -> dict[Tuple[type], Callable]:
        if item not in self.__cache:
            self.__cache[item] = {}
        return self.__cache[item]


def overload():
    """
    函数重载的实现

    :return:
    """
    _cache = OverloadCache()

    def are_types(types: tuple) -> bool:
        return all(type(t) == type for t in types)

    def call(*args, __key):
        overloads = _cache[__key]
        length = len(args)
        for arg_types, func in overloads.items():
            if len(arg_types) == length and all(isinstance(arg, t) for arg, t in zip(args, arg_types)):
                return func(*args)
        raise TypeError(f"No overload matches given arguments {args}")

    def init(*args_types: type):
        if not are_types(args_types):
            raise ValueError("arg types must be given as args of decorator")

        def dec(fn: Function):
            if fn.__code__.co_argcount != len(args_types):
                raise ValueError("number of args must match number of args_types")
            key = fn.__code__.co_filename, fn.__name__

            _cache[key][args_types] = fn
            return lambda *args: call(*args, __key=key)

        return dec

    return init


overload = overload()
