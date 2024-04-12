import time
from typing import Tuple, Type

from .to_decorator import toDecorator
from .._utils.exceptions import RetryFailed


def retry(
        times: int = 3,
        delay: float = 0,
        err: Tuple[Type[BaseException]] | Type[BaseException] = Exception
):
    """
    A decorator that can retry to call a failed function.
    :param times:
    :param delay:
    :param err:
    :return:
    """
    if callable(times):
        return retry()(times)
    if not isinstance(err, tuple):
        err = (err,)
    if not all(issubclass(e, BaseException) for e in err):
        raise ValueError("err must be a subclass of BaseException")

    @toDecorator
    def _retry(callback, *args, **kwargs):
        for i in range(times):
            try:
                return callback(*args, **kwargs)
            except err as e:
                print(f"{callback.__name__} failed, reason: {e}")
                if i != times - 1:
                    time.sleep(delay)
        raise RetryFailed(f"{callback.__name__} failed after {times} times")

    return _retry
