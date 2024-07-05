r"""OverloadFunctions"""

__all__ = ["OverloadFunction"]

import warnings
from enum import auto
from types import UnionType
from typing import Callable, Self, Dict, Tuple


class OverloadFunctionCache:
    def __init__(self):
        self.__cache: Dict[Tuple[type] | auto, Callable] = {}

    def __getitem__(self, *types):
        pass

    def default(self, *args):
        return


class OverloadFunction:
    r"""
    可重载的函数

    Example:
        >>> fn = OverloadFunction()
        >>> @fn.overload(int, int)
        ... def fn(a,b):
        ...     return a+b
        >>> @fn.overload(str, str)
        ... def fn(a,b):
        ...     return f"{a} str {b}"
        >>> fn(1,2)
        3
        >>> fn("Hello", "World")
        'Hello str World'
        >>> fn.lock()  # 锁定重载
        >>> fn(2,2)  # 可以正常调用
        4
        >>> @fn.overload(int)  # 锁定重载后不再能新增函数
        ... def fn(a):
        ...     return a * 2
        Traceback (most recent call last):
        RuntimeError: 此函数重载功能已被关闭
        >>> fn.unlock()
        >>> fn(1,"2")  # 未定义默认函数时若有未匹配的函数调用会报错
        Traceback (most recent call last):
        ValueError: 未找到与 (1, '2') 类型相匹配的重载函数
        >>> @fn.overload(OverloadFunction.DEFAULT)
        ... def fn(*args):
        ...     print(f"get: {args}")
        >>> fn(1,"2")  # 定义后则会交由定义的默认函数处理
        get: (1, '2')
        >>> fn.clear_default()
        >>> fn(1,"2")
        Traceback (most recent call last):
        ValueError: 未找到与 (1, '2') 类型相匹配的重载函数
    """

    DEFAULT = auto()
    DEFAULT_KEY = (DEFAULT,)

    def __init__(self):
        self.__overloads = {}
        self.__locked_overload = False

    def __call__(self, *args):
        if not args:
            fn = self.__overloads.get(tuple())
            if not fn:
                raise ValueError(f"未找到与 {args} 类型相匹配的重载函数")
            return fn()

        length = len(args)
        for types, func in self.__overloads.items():
            if len(types) == length and all(isinstance(arg, t) for arg, t in zip(args, types)):
                return func(*args)
        if OverloadFunction.DEFAULT_KEY in self.__overloads:
            return self.__overloads[OverloadFunction.DEFAULT_KEY](*args)

        raise ValueError(f"未找到与 {args} 类型相匹配的重载函数")

    def overload(self, *args_types: type | type(DEFAULT)) -> Callable[[...], Self]:
        if self.__locked_overload:
            raise RuntimeError("此函数重载功能已被关闭")

        if not self.__are_types(args_types):
            raise ValueError("OverloadFunction.overload() 必须传入重载函数的参数类型")

        def decorator(func):
            if args_types in self.__overloads:
                warnings.warn(f"已经存在参数为 {args_types} 的定义函数，之前的定义将会被覆盖", RuntimeWarning)
            self.__overloads[args_types] = func
            return self

        return decorator

    @staticmethod
    def __are_types(types):
        return (
                all(type(t) == type or type(t) == UnionType for t in types)
                or (len(types) == 1 and types[0] is OverloadFunction.DEFAULT)
        )

    def lock(self):
        """锁定重载，即不能再添加重载函数"""
        self.__locked_overload = True

    def unlock(self):
        self.__locked_overload = False

    def is_locked(self):
        return self.__locked_overload

    def clear_default(self):
        if OverloadFunction.DEFAULT_KEY not in self.__overloads:
            warnings.warn("默认函数未定义", RuntimeWarning)
            return
        del self.__overloads[OverloadFunction.DEFAULT_KEY]
