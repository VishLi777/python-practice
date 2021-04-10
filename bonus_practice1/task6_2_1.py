# Реализуйте аналогичную функцию fast_pow для возведения в степень
# (ее легко получить из предыдущего решения).


def fast_pow(x, y, r=1):
    while y > 0:
        if y == 1:
            return r * x
        if y % 2 != 0:
            r *= x
        x *= x
        y //= 2
    return r

