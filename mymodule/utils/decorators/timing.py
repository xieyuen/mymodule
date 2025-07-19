import time


def timing(output=None):
    def dec(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            output and output(f"function {func.__name__} took {end - start} seconds")
            return result
    return dec
