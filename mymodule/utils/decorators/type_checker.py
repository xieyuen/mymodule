def type_checker(
        *args_types,
        **kwargs_types,
):
    """
    Examples:
        >>> @type_checker(int, str, key=bool)
        ... def test(i, s, *, key):
        ...     print(i, s, key)
        >>> test(1,"2", key=True)
        1 2 True
        >>> test(1,2, key=None)
        Traceback (most recent call last):
        TypeError: 第 2 个参数类型错误: 应为 <class 'str'>, 实际为 <class 'int'>
        >>> test(1,"2", key="True")
        Traceback (most recent call last):
        TypeError: 参数 key 类型错误: 应为 <class 'bool'>, 实际为 <class 'str'>

    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            # position arguments
            for index, arg, arg_type in zip(range(len(args)), args, args_types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"第 {index+1} 个参数类型错误: 应为 {arg_type}, 实际为 {type(arg)}")

            # keyword arguments
            for key, value in kwargs.items():
                if key not in kwargs_types:
                    raise TypeError(f"未知参数: {key}")

                if not isinstance(value, kwargs_types[key]):
                    raise TypeError(f"参数 {key} 类型错误: 应为 {kwargs_types[key]}, 实际为 {type(value)}")

            return func(*args, **kwargs)

        return wrapper

    return decorator
