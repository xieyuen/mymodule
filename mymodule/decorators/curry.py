def curry(callback):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= callback.__code__.co_argcount:
            return callback(*args, **kwargs)
        else:
            return (
                lambda *more_args, **more_kwargs:
                curried(*args, *more_args, **kwargs, **more_kwargs)
            )

    return curried
