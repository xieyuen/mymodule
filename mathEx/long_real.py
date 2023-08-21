from typing import Tuple

from .real_num import Real


class LongReal:
    '''
    这是用来储存大数的实数类

    :param:`num` str, 储存数
    :param:`sym` str, 储存数的符号
    '''
    num: str
    sym: str


# --------------------------------------------------------------------------------------------------

# init 函数
def __init(self, num: int|float|str|Real|LongReal) -> LongReal:
    if type(num) != int and type(num) != float and type(num) != str \
        and type(num) != Real and type(num) != LongReal:

        raise TypeError('LongReal 类只能使用 int/float/str/Real/LongReal 类型对象进行初始化')

    # 科学计数法
    if e in str(num):
        raise ValueError('LongReal 类暂不支持科学计数法！')

    # LongReal
    if isinstance(num, LongReal):
        self = num
        return self

    # Real
    if isinstance(num, Real):
        self.num = str(num)
        self.sym = '+' if num > 0 else '-'
        return self

    try: int(num)
    except ValueError:
        # 在这里，所有类似 '-1-1'、'12345--++1765' 等等无法转化为数字的都会被挑出来
        raise ValueError('你输入的对象不是数字！')

    type_ = type(num)
    num = str(num)
    # 判断符号
    if num[0] == '-':
        self.sym = '-'
        num = num[1:]
    elif num[0] == '+':
        self.sym = '+'
        num = num[1:]
    else:
        self.sym = '+'

    # 去下划线 (_)
    if '_' in num: num = num.replace('_', '')

    num = type_(num)

    if isinstance(num, str):
        self.num = num
    elif int(num) == float(num):
        self.num = str(int(num))
    else:
        num = str(num)
        if num[-1] == '.':
            num += '0'
        if num[0] == '.':
            num = '0' + num
        self.num = num

    return self


def __repr(self) -> Tuple[str, str]:
    return self.sym, self.num

LongReal.__init__ = __init
LongReal.__repr__ = __repr

# --------------------------------------------------------------------------------------------------

# int, float, str, bool 方法的定义
def __int  (self) -> int:   return int(self.sym + self.num)
def __float(self) -> float: return float(self.sym + self.num)
def __str  (self) -> str:   return self.sym + self.num
def __bool (self) -> bool:  return True if self.num != '' else False


LongReal.__int__ = __int
LongReal.__float__ = __float
LongReal.__str__   = __str
LongReal.__bool__  = __bool


# --------------------------------------------------------------------------------------------------

# 基础一元运算和绝对值
def __neg(self) -> LongReal: return LongReal("-" + self.num)
def __pos(self) -> LongReal: return LongReal(self)
def __abs(self) -> LongReal: return LongReal(self.num)


LongReal.__neg__ = __neg
LongReal.__pos__ = __pos
LongReal.__abs__ = __abs


# --------------------------------------------------------------------------------------------------

# 数学运算(加、减、乘、除、模等等)
def __add(self, other: LongReal) -> LongReal:
    return \
        LongReal(self.num + other.num)  \
        if isinstance(other, LongReal) \
        else (
            LongReal(self.num + other)  
            if (isinstance(other, int) or isinstance(other, float)) 
            else NotImplemented
        )

def __sub(self, other: LongReal) -> LongReal:
    return \
        LongReal(self.num - other.num)  \
        if isinstance(other, LongReal) \
        else (
            LongReal(self.num - other)  
            if (isinstance(other, int) or isinstance(other, float)) 
            else NotImplemented
        )

def __mul(self, other: LongReal) -> LongReal:
    return \
        LongReal(self.num * other.num)  \
        if isinstance(other, LongReal) \
        else (
            LongReal(self.num * other)  
            if (isinstance(other, int) or isinstance(other, float)) 
            else NotImplemented
        )

def __div(self, other: LongReal) -> LongReal:
    return \
        LongReal(self.num / other.num)  \
        if isinstance(other, LongReal) \
        else (
            LongReal(self.num / other)  
            if (isinstance(other, int) or isinstance(other, float)) 
            else NotImplemented
        )

def __floordiv(self, other: LongReal) -> LongReal:
    return \
        LongReal(self.num // other.num) \
        if isinstance(other, LongReal) \
        else (
            LongReal(self.num // other) 
            if (isinstance(other, int) or isinstance(other, float)) 
            else NotImplemented
        )

def __truediv(self, other: LongReal) -> LongReal:
    return \
        LongReal(self.num / other.num)  \
        if isinstance(other, LongReal) \
        else (
            LongReal(self.num / other)  
            if (isinstance(other, int) or isinstance(other, float)) 
            else NotImplemented
        )

def __mod(self, other: LongReal) -> LongReal:
    return \
        LongReal(self.num % other.num)  \
        if isinstance(other, LongReal) \
        else (
            LongReal(self.num % other)  
            if (isinstance(other, int) or isinstance(other, float)) 
            else NotImplemented
        )

def __pow(self, other: LongReal) -> LongReal:
    return \
        LongReal(self.num ** other.num) \
        if isinstance(other, LongReal) \
        else (
            LongReal(self.num ** other) 
            if (isinstance(other, int) or isinstance(other, float)) 
            else NotImplemented
        )

def __divmod(self, other: LongReal) -> Tuple[LongReal, LongReal]: return (self.__div__(other), self.__mod__(other)) if isinstance(other, LongReal) else ((self.__div__(LongReal(other)), self.__mod__(LongReal(other))) if (isinstance(other, int) or isinstance(other, float)) else NotImplemented)

LongReal.__add__       = __add
LongReal.__sub__       = __sub
LongReal.__mul__       = __mul
LongReal.__div__       = __div
LongReal.__floordiv__  = __floordiv
LongReal.__truediv__   = __truediv
LongReal.__mod__       = __mod
LongReal.__pow__       = __pow
LongReal.__divmod__    = __divmod

def __radd     (self, other: LongReal) -> LongReal: return self.__add__(other)
def __rsub     (self, other: LongReal) -> LongReal: return self.__sub__(other)
def __rmul     (self, other: LongReal) -> LongReal: return self.__mul__(other)
def __rfloordiv(self, other: LongReal) -> LongReal: return self.__floordiv__(other)
def __rtruediv (self, other: LongReal) -> LongReal: return self.__truediv__(other)
def __rmod     (self, other: LongReal) -> LongReal: return self.__mod__(other)
def __rpow     (self, other: LongReal) -> LongReal: return self.__pow__(other)
def __rdivmod  (self, other: LongReal) -> Tuple[LongReal, LongReal]: return self.__divmod__(other)

LongReal.__radd__      = __radd
LongReal.__rsub__      = __rsub
LongReal.__rmul__      = __rmul
LongReal.__rfloordiv__ = __rfloordiv
LongReal.__rtruediv__  = __rtruediv
LongReal.__rmod__      = __rmod
LongReal.__rdivmod__   = __rdivmod
LongReal.__rpow__      = __rpow

# --------------------------------------------------------------------------------------------------

# 比较运算
def __eq(self: LongReal, other: int|float|LongReal) -> bool:
    return (self.num == other.num and self.sym == other.sym) \
        if isinstance(other, LongReal) \
        else (
            (
                (self.sym + self.num) == str(other)
            ) if isinstance(other, int) or isinstance(other, float)
            else NotImplemented
        )


def __lt(self: LongReal, other: int|float|LongReal) -> bool:
    # 小于
    return (  # is LongReal
        self.num < other.num
            if self.sym == other.sym
            else (
                False if other.sym == '+' else True
            )
        ) if isinstance(other, LongReal) \
        else (
            (  # is int or float
                (  # other > 0
                    True if self.sym == '-'
                    else (  # >0 and >0
                        ...
                    )
                )
                if str(other)[0] != '-'
                else (  # other > 0
                    False if self.sym == '+'
                    else (
                        ...
                    )
                )
            )
            if isinstance(other, int) or isinstance(other, float)
            else NotImplemented
        )


def __ne(self: LongReal, other: LongReal) -> bool:
    return not self.__eq__(other)


def __le(self: LongReal, other: LongReal) -> bool:
    return self.__lt__(other) or self.__eq__(other)


def __gt(self: LongReal, other: LongReal) -> bool:
    return not self.__le__(other)


def __ge(self: LongReal, other: LongReal) -> bool:
    return not self.__lt__(other)


LongReal.__eq__ = __eq
LongReal.__ne__ = __ne
LongReal.__lt__ = __lt
LongReal.__le__ = __le
LongReal.__gt__ = __gt
LongReal.__ge__ = __ge
