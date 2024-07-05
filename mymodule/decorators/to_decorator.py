from typing import Callable, Any


def toDecorator(dec: Callable[[Callable, ...], Any]) -> Callable:
    """
    有了它再也不用定义闭包了

    Examples:
        >>> @toDecorator
        ... def test_dec(callback, *args, **kwargs):
        ...     print(callback.__name__, args, kwargs)
        ...     return callback(*args, **kwargs)
        >>> @test_dec
        ... def test(a):
        ...     return a + 1
        >>> test(1)
        test (1,) {}
        > 2

    """

    def decorator(callback: Callable):
        def wrapper(*args, **kwargs):
            return dec(callback, *args, **kwargs)

        return wrapper

    return decorator
