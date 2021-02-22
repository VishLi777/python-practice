from math import sqrt, tan, cos, sin, exp

def f11(x,y):
    result = ((72*y-y**3)/(22*x**3+sin(y)))-sqrt(sin(y)+y)-sqrt((x**7 - y**4)/(sin(y)-exp(y)))
    return result


def f12(x):
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


def f13(n,m):
    result1=0
    result2=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            result1 +=(72*j-j**3)
    for i in range(1,n+1):
        result2 += (i**6 - tan(i))
    result = (24*result1-result2)
    return result


def f14(n):
    if n==0:
        return 3
    else:
        return (1/74)*f14(n-1)-(1/17)*(f14(n-1))**3
