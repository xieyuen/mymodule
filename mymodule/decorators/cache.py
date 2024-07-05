from .._utils.types import Function


class CacheInfo:
    def __init__(self, c: dict):
        self.__cache = c

    @property
    def length(self):
        return len(self.__cache)

    def __repr__(self):
        return f"CacheInfo(length={self.length})"


class cache:
    __callback: Function

    def __init__(self, fn):
        self.__callback = fn
        self.__cache = {}
        self.__info = CacheInfo(self.__cache)

    @property
    def __code__(self):
        return self.__callback.__code__

    def __call__(self, *args, **kwargs):
        key = f"({args}, {kwargs})"
        if key not in self.__cache:
            self.__cache[key] = self.__callback(*args, **kwargs)
        return self.__cache[key]

    def clear(self):
        self.__cache.clear()

    def info(self):
        return self.__info
