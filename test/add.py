from mymodule.utils.overload_function import OverloadFunction

add: OverloadFunction = OverloadFunction()
add.__annotations__ = {
    "a": int | str,
    "b": int | str,
    "return": str,
}


@add.overload(int, int)
def add(a, b) -> str:
    return "{}".format(a + b)


@add.overload(str, str)
def add(a, b) -> str:
    length = max(len(a), len(b))

    a = [int(c) for c in a[::-1]]
    a += [0] * (length - len(a))
    b = [int(c) for c in b[::-1]]
    b += [0] * (length - len(b))
    result = [0] * (length + 1)

    for i in range(length):
        result[i] += a[i] + b[i]
        result[i + 1] += result[i] // 10
        result[i] %= 10

    return ''.join(str(c) for c in result[::-1]).strip("0")


# expose(add)

if __name__ == '__main__':
    print(add(
        1234, 4321
    ))
    print(add.__annotations__)
