# Привести примеры кода, которые соответствуют следующим нарушениям PEP 8:
# 1. whitespace before '('.
a = pow (base=7, exp=17)


# 2. missing whitespace around operator.
a=pow(base=7, exp=17)


# 3. missing whitespace after ','.
a = pow(base=7,exp=17)


# 4. unexpected spaces around keyword / parameter equals.
def t4(x = 2):
    print(x)

# 5. expected 2 blank lines, found 1.
def t5_1(x):
    print(x)

def t5_2(x):
    print(x)


# 6. multiple statements on one line (colon).
if a < 7:  a = t5_2(a)


# 7. multiple statements on one line (semicolon).
a = 1; a = 2


# 8. comparison to None should be 'if cond is None:'.
if a == None:
    a = 1
    print(a)


# 9. comparison to True should be 'if cond is True:' or 'if cond:'.
if b == True:
    b = 7