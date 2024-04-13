def bind(fn, *bind_args, **bind_kwargs):
    return lambda *args, **kwargs: fn(*bind_args, *args, **bind_kwargs, **kwargs)


def getOptions(opt: dict, default: dict) -> dict:
    result = default.copy()
    result.update(opt)
    return result
