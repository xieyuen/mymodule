from typing import Callable, TypeVar

from .to_decorator import toDecorator

ARGS = TypeVar("ARGS")
BIND_ARGS = TypeVar("BIND_ARGS")
KWARGS = TypeVar("KWARGS")
BIND_KWARGS = TypeVar("BIND_KWARGS")


def bind(
        *bind_args: BIND_ARGS,
        **bind_kwargs: BIND_KWARGS,
) -> Callable[
    [
        Callable[[ARGS, KWARGS], ...]
    ],
    Callable[[BIND_ARGS, ARGS, BIND_KWARGS, KWARGS], ...]
]:
    """
    绑定参数到函数上

    Examples:
        >>> @bind(1, c=3)
        ... def test(a, b, c):
        ...     print(a, b, c)
        ...     return a, b, c
        >>> test(2)
        1 2 3
        (1, 2, 3)

        >>> def test(a, b, c):
        ...     print(a, b, c)
        ...     return a, b, c
        >>> bound_test = bind(1, c=4)(test)
        >>> bound_test()
        1 2 3
        (1, 2, 3)
    """

    @toDecorator
    def bound(callback, *args, **kwargs):
        return callback(*bind_args, *args, **bind_kwargs, **kwargs)

    return bound
