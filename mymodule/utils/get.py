from typing import List, Any


def in_(key, obj):
    return (
            (key in obj)
            or (f"{key}".isdigit() and 0 <= key < len(obj))  # for list
    )


def get(obj, path: str | List, default=None) -> Any:
    """
    lodash get()

    :param obj:
    :param path:
    :param default:
    :return:
    """
    if not isinstance(path, (list, str)):
        raise TypeError("arg:path must be a string or list")

    if isinstance(path, str):
        path = path.split('.')

    for key in path:
        if not in_(key, obj):
            return None
        obj = obj[key]

    if not in_(key, obj):
        return default
    return obj[key]
