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


def f22(x):
    H = x & 0x80000000
    G = x & 0x40000000
    F = x & 0x20000000
    E = x & 0x18000000
    D = x & 0x07000000
    C = x & 0x00c00000
    B = x & 0x003F0000
    A = x & 0x0000FFFF
    H = H
    G = G
    F = F>>26
    E = E>>7
    D = D>>24
    C = C
    B = B<<8
    A = A<<4
    x = A + B + C + D + E + F + G + H
    return x