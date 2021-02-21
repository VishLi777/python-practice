print("Practice1.3")


def f3(n,m):
    result1=0
    result2=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            result1 +=(72*j-j**3)
    for i in range(1,n+1):
        result2 += (i**6 - tan(i))
    result = (24*result1-result2)
    return result


print("{:.2e}".format(f3(82,22)))
print("{:.2e}".format(f3(46,53)))


