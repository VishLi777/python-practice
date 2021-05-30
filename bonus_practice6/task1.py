from math import sin, cos, pi
from functools import reduce
import operator


def deriv(func):
    def _der(x, h=0.0001):
        return (func(x + h) - func(x - h)) / (2 * h)

    return _der


print(deriv(lambda x: x ** 3)(5))


def make_perf(data):
    def wrap(f):
        def g(*args, **kwargs):
            if f.__name__ in data:
                data[f.__name__] += 1
            else:
                data[f.__name__] = 1
            return f(*args, **kwargs)

        return g

    return wrap


def memo(f):
    cashe = {}

    def wrap(*args, **kwargs):
        key = tuple(args)
        if key not in cashe:
            cashe[key] = f(*args, **kwargs)
        return cashe[key]

    return wrap


PERF = {}
perf = make_perf(PERF)


@memo
@perf
def foo(x):
    print(x)


@memo
@perf
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


foo(1)
foo(2)
foo(1)
print(fib(27))
print(PERF)

print((lambda x: reduce(operator.mul, range(1, x + 1), 1))(10))