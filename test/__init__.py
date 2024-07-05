from mymodule import toDecorator, bind


def testDec(callback, *args, **kwargs):
    print("before")
    result = callback(*args, **kwargs)
    print("after")
    return result


@bind(456)
@toDecorator(testDec)
def test(a, b):
    print(a, b)
    return a


def main():
    print(test(123))


if __name__ == '__main__':
    main()
