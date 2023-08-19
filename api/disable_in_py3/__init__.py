__all__ = [
    'cmp'
]


def cmp(x: int|float, y: int|float) -> int:
    return (x > y) - (x < y)
