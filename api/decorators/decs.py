# Decorators
import time

from ...utils import logger


def elapsed_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        logger.info(f'运行用时: {end - start} 秒')
    return wrapper


def ignore(func):
    logger.info('function/method {} was ignored.'.format(func.__name__))
    return None


delete = ignore
