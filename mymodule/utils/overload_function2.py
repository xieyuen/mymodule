import warnings

from mymodule._utils.types import Types, Function

__all__ = ["OverloadFunction", "DEFAULT", "SELF"]


class DEFAULT:
    def __instancecheck__(self, instance):
        return True


DEFAULT = DEFAULT()


class SELF:
    def __instancecheck__(self, instance):
        return True


SELF = SELF()


def instanceof_type(t):
    return isinstance(t, Types) or issubclass(type(t), type) or t is SELF


class OverloadCache:
    def __init__(self):
        self.__cache: dict[tuple[type], Function] = {}

    def __setitem__(self, types, function):
        self.__cache[types] = function

    def default(self, *args):
        return self.__cache[(DEFAULT,)](*args)

    def has_default(self):
        return (DEFAULT,) in self.__cache

    def get_and_call(self, *args):
        for types, f in self.__cache.items():
            if all(isinstance(arg, t) for t, arg in zip(types, args)):
                return f(*args)
        if not self.has_default():
            raise ValueError(f"没有找到匹配的函数: {args}")
        self.default(*args)


class OverloadFunction:
    r"""
        可重载的函数——新实现

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
            >>> @fn.overload(DEFAULT) # 用 DEFAULT 声明，此时不再接受参数类型
            ... def fn(*args):
            ...     print(f"get: {args}")
            >>> fn(1,"2")  # 定义后则会交由定义的默认函数处理
            get: (1, '2')
            >>> class Test:
            ...     @OverloadFunction().overload(SELF, int,int)
            ...     def test(self, a, b):
            ...         print(f"got int: {a} {b}")
            ...     @test.overload(SELF, str,str)
            ...     def test(self, a, b):
            ...         print(f"got str: {a} {b}")
            >>> t = Test()
            >>> t.test(1,2)
            got int: 1 2
            >>> t.test("3","4")
            got str: 3 4
        """

    def __init__(self):
        self.__cache = OverloadCache()

    def overload(self, *types):
        if len(types) == 1 and callable(types[0]):
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
        return self.__cache.get_and_call(*args)


def test():
    class Test:
        t = OverloadFunction()

        @t.overload(SELF, int, int)
        def t(self, a):
            print(f"got int: {self} {a}")

        @t.overload(SELF, str, str)
        def t(self, a):
            print(f"got str: {self} {a}")

    t = Test()
    t.t(1, 2)
    t.t("3", "4")


if __name__ == '__main__':
    test()
