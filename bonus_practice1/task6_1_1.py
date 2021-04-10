# Реализуйте функцию fast_mul в соответствии с алгоритмом двоичного умножения в столбик.
# Добавьте автоматическое тестирование, как в случае с naive_mul.


def fast_mul(x, y):
    if x == 0 or y == 0:  # add condition
        return 0
    r = 0  # r = 1
    while y > 0:
        if y % 2 == 1:
            r += x
        x *= 2
        y //= 2
    return r



