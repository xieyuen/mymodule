def get_options(
        options: dict[str, ...],
        defaults: dict[str, ...],
        *,
        check_type: bool = True
) -> dict:
    """为参数设置默认值"""
    result = defaults.copy()
    if not check_type:
        result.update(options)
        return result

    for key, value in options.items():
        if key in defaults and not isinstance(value, type(defaults[key])):
            continue
        result[key] = value

    return result


def _test(**options):
    option = get_options(options, {
        "foo": "bar",
        "baz": [1, 2],
        "qux": {"hello": "world"}
    },  check_type=True
    )

    print(option)
    option["baz"].append(3)
    option["qux"]["new key"] = "new value"
    print(option)


if __name__ == '__main__':
    _test(abc=1, baz=1234)
