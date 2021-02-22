print("Practice2.2")


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
    x = hex(int(A + B + C + D + E + F + G + H))
    return x


print(f22(0xed6c6d05))
print(f22(0x3cff94d4))





