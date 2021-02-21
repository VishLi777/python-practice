print("Practice1.4")

def rec(n):
    if n==0:
        return 3
    else:
        return (1/74)*rec(n-1)-(1/17)*(rec(n-1))**3


print("{:.2e}".format(rec(7)))
print("{:.2e}".format(rec(5)))
