#print("Practice2.1")


def f21(x):
    if x[1] == 'nesc':
        if x[0] == 2003:
            if x[2] == 'tcl':
                return 0
            elif x[2] == 'arc':
                return 1
        elif x[0] == 2008:
            if x[2] == 'tcl':
                return 2
            elif x[2] == 'arc':
                return 3
    elif x[1] == 'bro':
        if x[3] == 'json5':
            if x[0] == 2003:
                return 4
            elif x[0] == 2008:
                return 5
        elif x[3] == 'm':
            if x[2] == 'tcl':
                return 6
            elif x[2] == 'arc':
                return 7
        elif x[3] == 'gdb':
            if x[0] == 2003:
                return 8
            elif x[0] == 2008:
                return 9
    elif x[1] == 'ebnf':
        return 10
    else:
        return None


print(f21([2003, 'nesc', 'arc', 'm']))
print(f21([2003, 'bro', 'arc', 'json5']))



