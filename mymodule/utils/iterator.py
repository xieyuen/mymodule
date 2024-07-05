__all__ = ["Iterator"]


class IteratorReturn:
    def __init__(self, value, done):
        self.value = value
        self.done = done

    def __getitem__(self, item):
        if item == "value":
            return self.value
        elif item == "done":
            return self.done
        else:
            raise KeyError(f"Invalid key: {item}")

    def unpack(self):
        return self.done, self.value

    def __repr__(self):
        return f"IteratorReturn(value={self.value}, done={self.done})"

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index == 0:
            self.__index += 1
            return self.value
        elif self.__index == 1:
            self.__index += 1
            return self.done
        else:
            del self.__index
            raise StopIteration


class Iterator:
    def __init__(self, iter_object):
        self.__origin = iter_object
        self.__iter_object = iter(iter_object)
        self.__done = False

    def __iter__(self):
        self.__iter_object = iter(self.__origin)
        return self

    def __next__(self):
        if self.__done:
            raise StopIteration
        try:
            v = next(self.__iter_object)
        except StopIteration:
            self.__done = True
            return IteratorReturn(None, True)
        else:
            return IteratorReturn(v, False)

    def next(self):
        return next(self)

    def __getitem__(self, item):
        return self.__origin[item]

    def __repr__(self):
        return f"<Iterator({self.__origin}) at {hex(id(self))}>"


if __name__ == '__main__':
    def p(i):
        print([item for item in dir(i) if item.startswith("_") and not item.startswith("__")])


    i = Iterator([1, 2, 3])

    for r in i:
        print(dir(r))
        p(i)
