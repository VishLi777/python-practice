# x += x ----> x = x + x


# def multiply_by_add12(x) - функция, с помощью которой осуществляется умножение на 12. 4 сложения.
def multiply_by_add12(x):
    x += x + x
    x += x
    x += x
    return x


print(multiply_by_add12(1))


# def multiply_by_add16(x) - функция, с помощью которой осуществляется умножение на 16. 4 сложения.
def multiply_by_add16(x):
    x += x
    x += x
    x += x
    x += x
    return x


print(multiply_by_add16(1))


# def multiply_by_add15(x) - функция, с помощью которой осуществляется умножение на 15. 3 сложения и 2 вычитания.
def multiply_by_add15(x):
    a = x
    x += x
    x += x
    x += x
    x = x - (-x) - a
    return x


print(multiply_by_add15(1))


# def multiply_by_add29(x) - функция, с помощью которой осуществляется умножение на 29. 6 сложений и одно вычитание.
def multiply_by_add29(x):
    a = x
    x += x
    x += x
    x += a
    x += x + x
    x += x
    x = x - a
    return x


print(multiply_by_add29(1))