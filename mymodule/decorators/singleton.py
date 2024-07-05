from typing import NoReturn


def singleton(cls):
    """
    单例模式的装饰器实现
    Examples:
        >>> @singleton
        ... class TestSingleton:
        ...     pass
        >>> a = TestSingleton()
        >>> b = TestSingleton()
        >>> a is b, a == b
        (True, True)
    """
    _instance = None

    def _getInstance(*args, **kwargs):
        nonlocal _instance
        if _instance is None:
            _instance = cls(*args, **kwargs)
        return _instance

    return _getInstance


class singleton2:
    __cls: type
    __instance: object

    def __init__(self, cls: type, *, expose: bool = False):
        self.__cls = cls
        self.__instance = None
        self.__name__ = cls.__name__

        self.__expose = expose

    @property
    def cls(self) -> __cls | NoReturn:
        if not self.__expose:
            raise RuntimeError(f"class {self.__cls.__name__} hasn't been exposed")
        return self.__cls

    def __call__(self, *args, **kwargs):
        if not self.__instance:
            self.__instance = self.__cls(*args, **kwargs)
        return self.__instance

# export(singleton, singleton2)
