def get_options(
        options: dict[str, ...],
        defaults: dict[str, ...],
        *,
        check_type: bool = True,
        limit_size: bool = False,
) -> dict:
    """为参数设置默认值"""
    result = defaults.copy()
    if limit_size:
        for key, value in options.items():
            if key not in defaults:
                continue
            if check_type and not isinstance(value, type(defaults[key])):
                continue
            result[key] = value

    if not check_type:
        result.update(options)
        return result

    for key, value in options.items():
        if key in defaults and not isinstance(value, type(defaults[key])):
            continue
        result[key] = value

    return result
