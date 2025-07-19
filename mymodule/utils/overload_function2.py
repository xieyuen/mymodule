import warnings

from mymodule.types import Types, Function

__all__ = ["OverloadFunction", "DEFAULT"]


class DEFAULT:
    def __instancecheck__(self, instance):
        return True


DEFAULT = DEFAULT()


class EMPTY:
    def __instancecheck__(self, instance):
        return True


EMPTY = EMPTY()


def instanceof_type(t):
    return (
            isinstance(t, Types)
            or issubclass(type(t), type)
            or t is DEFAULT
            or t is EMPTY
    )


class OverloadCache:
    def __init__(self):
        self.__cache: dict[tuple[type], Function] = {}

    def __setitem__(self, types, function):
        self.__cache[types] = function

    def default(self, *args):
        return self.__cache[(DEFAULT,)](*args)

    def has_default(self):
        return (DEFAULT,) in self.__cache

    def call(self, *args):
        if not args:
            if (EMPTY,) not in self.__cache:
                raise ValueError("未找到无参重载函数")
            return self.__cache[(EMPTY,)]()
        for types, f in self.__cache.items():
            if all(isinstance(arg, t) for t, arg in zip(types, args)):
                return f(*args)
        if not self.has_default():
            raise ValueError(f"未找到与 {args} 类型相匹配的重载函数")
        return self.default(*args)


class OverloadFunction:
    r"""
        可重载的函数——新实现, 但是不支持柯里化

        Example:
            >>> fn = OverloadFunction()
            >>> @fn.overload(int, int)
            ... def fn(a,b):
            ...     return a + b
            >>> @fn.overload(str, str)
            ... def fn(a,b):
            ...     return f"{a} str {b}"
            >>> fn(1,2)
            3
            >>> fn("Hello", "World")
            'Hello str World'
            >>> fn(2,2)
            4
            >>> fn(1,"2")  # 未定义默认函数时若有未匹配的函数调用会报错
            Traceback (most recent call last):
            ValueError: 未找到与 (1, '2') 类型相匹配的重载函数
            >>> fn()
            Traceback (most recent call last):
            ValueError: 未找到无参重载函数
            >>> @fn.overload()  # 无参函数的定义
            ... def fn():
            ...    print("hello world")
            >>> fn()
            hello world
            >>> @fn.overload(DEFAULT) # 用 DEFAULT 声明，此时不再接受参数类型
            ... def fn(*args):
            ...     print(f"get: {args}")
            >>> fn(1,"2")  # 定义后则会交由定义的默认函数处理
            get: (1, '2')
            >>> fn("Hello", "World") # 不影响原有的重载函数
            'Hello str World'
        """

    def __init__(self):
        self.__cache = OverloadCache()

    def overload(self, *types):
        if not types:
            types = (EMPTY,)
        elif len(types) == 1 and callable(types[0]):
            if types[0].__code__.co_arguments == 0:
                raise ValueError("非无参函数需要传入参数类型")
            return self.overload()(types[0])
        elif types[0] is DEFAULT and len(types) != 1:
            warnings.warn("声明为 DEFAULT 函数时无需传入参数类型")
            types = (DEFAULT,)
        elif not all(instanceof_type(t) for t in types):
            raise ValueError("传入了错误的类型")

        def decorator(function: Function):
            self.__cache[types] = function
            return self

        return decorator

    def __call__(self, *args):
        return self.__cache.call(*args)
