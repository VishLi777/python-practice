from math import sqrt, tan, cos, sin, exp
print("Practice1.1")


def pr1(x,y):
    result = ((72*y-y**3)/(22*x**3+sin(y)))-sqrt(sin(y)+y)-sqrt((x**7 - y**4)/(sin(y)-exp(y)))
    return result


print("{:.2e}".format(pr1(-20,51)))
print("{:.2e}".format(pr1(-1,56)))


