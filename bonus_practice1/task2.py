# Объяснение странного выражения и странного результата
# true = 1
# false = 0
# -true = -1


# 1 * 2 = 2
print(True * 2)


# 1 * 2 + 0 = 2
print(True * 2 + False)


# (1 * 2) * 1 = 2
print((True * 2) * True)


# (1 * 2 + 0) * (-1) = -2  --> -2
print((True * 2 + False) * -True)


