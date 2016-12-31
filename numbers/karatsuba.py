import math

BASE = 10

def digits(x):
    return int(math.log10(x)) + 1

def karatsuba(x, y):
    if x < BASE or y < BASE:
        return x * y
    
    deg = max(digits(x), digits(y))
    exp = deg // 2

    x1 = x // BASE ** exp
    x0 = x % BASE ** exp
    y1 = y // BASE ** exp
    y0 = y % BASE ** exp

    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x0 + x1, y0 + y1)
    z2 = karatsuba(x1, y1)

    return z2 * BASE ** (exp * 2) + (z1 - z2 - z0) \
        * BASE ** exp + z0
