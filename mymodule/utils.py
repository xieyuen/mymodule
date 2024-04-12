def bind(fn, *bind_args, **bind_kwargs):
    return lambda *args, **kwargs: fn(*bind_args, *args, **bind_kwargs, **kwargs)
