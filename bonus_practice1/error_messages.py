import math

# 1. SyntaxError: cannot assign to literal
def cannot_assign_to_literal():
    "python" = "Java"


# 2. SyntaxError: invalid syntax
def invalid_syntax():
    try:
        print (""
    except BaseException as e:
        print(e)


# 3. NameError: name ... is not defined
def name_is_not_defined():
    checker = 77


    print(check)


# 4. TypeError: unsupported operand type(s) for ...
def unsupported_operand_type():
    check = "helloworld" - 7


# 5. IndentationError: expected an indented block
def indented_block():
    def big_number(seven, ten):
        if seven < ten:
    return ten
    else:
    return seven


# 6. ZeroDivisionError: division by zero
def division_by_zero():
    return 777 / 0


# 7. ValueError: math domain error
def math_domain_error():
    return math.log(0)


# 8. OverflowError: math range error
def math_range_error():
    val = '7' * 777
    print(math.pow(int(val), math.e))


if __name__ == '__main__':

    print()

    # print(name_is_not_defined())
    # print(unsupported_operand_type())
    # print(division_by_zero())
    # print(math_domain_error())
    # print(math_range_error())
