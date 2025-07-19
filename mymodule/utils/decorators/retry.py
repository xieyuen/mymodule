import time
from typing import Tuple, Type

from mymodule.utils.decorators.to_decorator import to_decorator
from mymodule.exceptions import RetryFailedError


def retry(
        times: int = 3,
        delay: float = 0,
        *,
        err: Tuple[Type[BaseException]] | Type[BaseException] = Exception,
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

    @to_decorator
    def _retry(callback, *args, **kwargs):
        for i in range(times):
            try:
                return callback(*args, **kwargs)
            except err as e:
                print(f"{callback.__name__} failed, reason: {e}")
                if i != times - 1:
                    time.sleep(delay)
        raise RetryFailedError(f"{callback.__name__} failed after {times} times")

    return _retry
