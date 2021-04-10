# Некто попытался реализовать "наивную" функцию умножения с помощью сложений.
# К сожалению, в коде много ошибок. Сможете ли вы их исправить?


def naive_mul(x, y):
    if x == 0 or y == 0:  # add condition
        return 0
    r = x  # r = 1
    for i in range(0, y - 1):
        x = x + r
    return x


print(naive_mul(10, 15))