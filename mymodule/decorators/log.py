from .to_decorator import toDecorator
from ..utils import getOptions


def log(logger, **options):
    options = getOptions(
        options,
        {
            "log_start": False,
            "start_msg": 'function {name} start',
            "log_finish": False,
            "finish_msg": 'function {name} finished',
            "err_msg": 'function {name} raised an exception: {err}',
        }
    )
    log_start = options['log_start']
    start_msg = options['start_msg']
    log_finish = options['log_finish']
    finish_msg = options['finish_msg']
    err_msg = options['err_msg']

    @toDecorator
    def wrapper(callback, *args, **kwargs):
        # consts
        name = callback.__name__

        if log_start:
            logger.debug(start_msg.format(name=name))

        try:
            result = callback(*args, **kwargs)
        except Exception as err:
            logger.error(err_msg.format(name=name, err=err))
            raise

        if log_finish:
            logger.debug(finish_msg.format(name=name))

        return result

    return wrapper
