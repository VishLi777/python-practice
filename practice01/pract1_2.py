print("Practice1.2")


def f(x):
    if x < 111:
        result1 = 43*(cos(x)+x**6)**6-37*x**5
        return result1
    elif x < 204:
        result2 = (x**8/43) - 25*x**2 - 54
        return result2
    elif x < 294:
        result3 = 85*x - abs(x)
        return result3
    elif x >= 294:
        result4 = exp(x**6) - cos(x) + 42
        return result4


print("{:.2e}".format(f(227)))
print("{:.2e}".format(f(235)))


