from typing import Tuple, TypeVar

from HPA.string import HighPrecisionAlgorithms as Hpa


HPA = Hpa()
LR = TypeVar("LR")


class LongReal:
    """
    这是用来储存大数的实数类

    Attributes:
        abs: 储存数
        sym: 储存数的符号
    """
    abs: str
    sym: str

    def __init__(self, num: int | float | str | LR):
        if not (
            isinstance(num, int) or
            isinstance(num, float) or
            isinstance(num, str) or
            isinstance(num, LongReal)
        ):
            raise TypeError('LongReal 类只能使用 int/float/str/Real/LongReal 类型对象进行初始化')

        # 科学计数法
        if 'e' in str(num):
            raise ValueError('LongReal 类暂不支持科学计数法！')

        # LongReal
        if isinstance(num, LongReal):
            self.sym, self.abs = num.sym, num.abs
            return

        try:
            int(num)
        except ValueError:
            # 在这里，所有类似 '-1-1'、'12345--++1765' 等等无法转化为数字的 str 都会被挑出来
            raise ValueError('你输入的对象不是数字！')

        num_str = str(num)
        # 判断符号
        if num_str[0] == '-':
            self.sym = '-'
            num_str = num_str[1:]
        elif num_str[0] == '+':
            self.sym = '+'
            num_str = num_str[1:]
        else:
            self.sym = '+'

        num = type(num)(num_str)

        # 去下划线 (_)
        if '_' in num:
            num = num.replace('_', '')

        if isinstance(num, str):
            self.abs = num
        elif int(num) == float(num):
            self.abs = str(int(num))
        else:
            num = str(num)
            if num[-1] == '.':
                num += '0'
            if num[0] == '.':
                num = '0' + num
            self.abs = num

    def __repr__(self): return f'LongReal({self.sym + self.abs})'

    # --- int, float, str, bool 方法的定义 --- #
    def __int__(self) -> int: return int(self.sym + self.abs)
    def __float__(self) -> float: return float(self.sym + self.abs)
    def __str__(self) -> str: return self.sym + self.abs
    def __bool__(self) -> bool: return True if self.abs != '0' else False

    # --- 基础一元运算和绝对值 --- #
    def __neg__(self) -> LR: return LongReal("-" + self.abs) if self.sym == "+" else LongReal(self.abs)
    def __pos__(self) -> LR: return self
    def __abs__(self) -> LR: return LongReal(self.abs)

    # --- 比较运算 --- #
    def __eq__(self, other: int | float | LR) -> bool:
        return (self.abs == other.abs and self.sym == other.sym) \
            if isinstance(other, LongReal) \
            else (
            (
                (self.sym + self.abs) == str(other)
            ) if isinstance(other, int) or isinstance(other, float)
            else NotImplemented
        )

    def __lt__(self, other: int | float | LR) -> bool:
        if isinstance(other, LongReal):
            if self.sym == other.sym:  # 符号是否相同
                return self.abs < other.abs

            else:
                # 符号不同正为大
                return True if other.sym == '+' else False

        if not (isinstance(other, int) or isinstance(other, float)):
            return NotImplemented

        if isinstance(other, int):
            other_str = str(other)

            if other_str[0] == '-':
                # 切掉负号
                other_str = other_str[1:]

                # other 是一个负数
                if self.sym == '+':
                    return True

                return self.abs > other_str

            else:  # >0
                if self.sym == '-':
                    return True

                return self.abs < other_str

        if isinstance(other, float):
            other_int, other_dec = str(other).split('.')

            if other_int[0] == '-':
                if self.sym == '+':
                    return False

                # 切掉负号
                other_int = other_int[1:]

                try:
                    self_int, self_dec = self.abs.split('.')
                except ValueError:
                    # 当 self.num 是一个整数时
                    # 对整数部分先比较
                    if len(self.abs) > len(other_int):
                        return True
                    elif len(self.abs) < len(other_int):
                        return False

                    for self_char, other_char in zip(self.abs, other_int):
                        if self_char == other_char:
                            continue
                        if int(self_char) > int(other_char):
                            return True
                        else:
                            return False

                    # 若整数部分相等,
                    # 则当且仅当 other 的小数部分为 0 时，self.num < other == False
                    return False \
                        if other_dec == '0' \
                        else True

                if len(self_int) > len(other_int):
                    return True
                elif len(self_int) < len(other_int):
                    return False

                for self_char, other_char in zip(self_int, other_int):
                    if self_char == other_char:
                        continue
                    if int(self_char) > int(other_char):
                        return True
                    else:
                        return False

                # 若整数部分相等, 比较小数部分
                # 小数部分长度不相等时，要补齐
                max_len = max(len(self_dec), len(other_dec))

                self_dec += '0' * (max_len - len(self_dec))
                other_dec += '0' * (max_len - len(other_dec))

                for self_char, other_char in zip(self_dec, other_dec):
                    if self_char == other_char:
                        continue
                    if int(self_char) > int(other_char):
                        return True
                    else:
                        return False

                return False

    def __ne__(self, other: LR) -> bool: return not self.__eq__(other)
    def __le__(self, other: LR) -> bool: return self.__lt__(other) or self.__eq__(other)
    def __gt__(self, other: LR) -> bool: return not self.__le__(other)
    def __ge__(self, other: LR) -> bool: return not self.__lt__(other)

    # --- 基本数学运算(加、减、乘、除、乘方等等) --- #
    def __add__(self, other: LR) -> LR:
        if (
            isinstance(other, int) or
            isinstance(other, float)
        ):
            return self + LongReal(other)

        if not isinstance(other, LongReal):
            return NotImplemented

        if self.sym == other.sym:
            sym = self.sym
            res = HPA.add(self.abs, other.abs)
            return LongReal(sym + res)
        elif self.sym == '+':
            return self - other
        else:
            return other - self

    def __sub__(self, other: LR) -> LR:
        pass

    def __mul__(self, other: LR) -> LR:
        pass

    def __floordiv__(self, other: LR) -> LR:
        pass

    def __truediv__(self, other: LR) -> LR:
        pass

    def __mod__(self, other: LR) -> LR:
        pass

    def __pow__(self, other: LR) -> LR:
        pass

    def __div__(self, other: LR) -> LR: return self.__truediv__(other)

    def __divmod__(self, other: LR) -> Tuple[LR, LR]: return self.__truediv__(other), self.__mod__(other)

    def copy(self) -> LR: return LongReal(self)
