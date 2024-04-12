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
