# Объяснения цепочек сравнения

# 5 > 1 and 5 < 10   --> True
x = 5
print(1 < x < 10)  # True


# 5 < 10 --> True
# True = 1
# 1 < 1 ---> False
print(1 < (x < 10))  # False
