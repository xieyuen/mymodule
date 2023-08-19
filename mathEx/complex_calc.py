from math import sin, cos, atan, sqrt, pi


def complex_triangular_to_general(r: 'real', theta: 'real') -> complex:
    Re = r * cos(theta)
    Im = r * sin(theta)
    return Re + Im * 1j


def complex_sqrt(x: complex|int|float) -> complex|float:
    '''复数开平方'''
    # 数值分离：
    # 非负数直接使用 math.sqrt()
    if type(x) != complex or x.imag == 0:
        if isinstance(x, complex): x = x.real
        if x >= 0: return sqrt(x)

    # 传下来的数都是复数或负数
    # 全部转化为复数    
    x = complex(x)

    # 计算被开方数的辐角
    # 取主值即可
    if x.real == 0:
        arg = pi / 2
        if x.imag < 0: arg = -arg
    elif x.imag == 0:
        arg = pi
    else:
        arg = atan(x.imag / x.real)
    if x.real < 0: arg += pi

    # 计算被开方数的模
    # r = \sqrt{Re(x) ^ 2 + Im(x) ^ 2}
    r = abs(x)

    return complex_triangular_to_general(sqrt(r), arg/2)


