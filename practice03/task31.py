import struct


def f31(binary: bytes) -> dict:
    def struct_a(offset: int) -> dict:
        [k] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        [offset1] = struct.unpack('> I', binary[offset: offset + 4])
        st = '>' + str(k) + 's'
        a1 = [struct.unpack(st, binary[offset1: offset1 + k])]
        a1 = str(a1)[4:-4:]
        offset += 4


        [a2] = struct.unpack('> i', binary[offset: offset + 4])
        offset += 4

        a3 = struct_b(offset)
        offset += 4 + 9 + 8


        a4 = [struct_f(offset + i * 10) for i in range(3)]
        offset += 30

        return {
            'A1': a1,
            'A2': a2,
            'A3': a3,
            'A4': a4,

        }

    def struct_b(offset: int) -> dict:
        [b1] = struct.unpack('> L', binary[offset: offset + 4])
        offset += 4

        b2 = struct_e(offset)
        offset += 2 + 2 + 1 + 4
        [b3] = struct.unpack('> q', binary[offset: offset + 8])
        offset += 8

        return {
            'B1': struct_c(b1),
            'B2': b2,
            'B3': b3,

        }

    def struct_c(offset: int) -> dict:
        [c1] = struct.unpack('> f', binary[offset: offset + 4])
        offset += 4
        [c2] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        c3 = struct_d(offset)
        offset += 1 + 2 + 2 + 8 + 2
        c4 = list(struct.unpack('> 4B', binary[offset: offset + 4]))
        offset += 4
        [c5, c6] = struct.unpack('> 2l', binary[offset: offset + 8])
        offset += 8

        return {
            'C1': c1,
            'C2': c2,
            'C3': c3,
            'C4': c4,
            'C5': c5,
            'C6': c6,
        }

    def struct_d(offset: int) -> dict:
        [d1] = struct.unpack('> b', binary[offset: offset + 1])
        offset += 1
        [d2, d3] = struct.unpack('> 2h', binary[offset: offset + 4])
        offset += 4
        [d4] = struct.unpack('> d', binary[offset: offset + 8])
        offset += 8
        [d5] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2

        return {
            'D1': d1,
            'D2': d2,
            'D3': d3,
            'D4': d4,
            'D5': d5,
        }

    def struct_e(offset: int) -> dict:
        [e1] = struct.unpack('> h', binary[offset: offset + 2])
        offset += 2
        [e2] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        [e3] = struct.unpack('> B', binary[offset: offset + 1])
        offset += 1
        [e4] = struct.unpack('> i', binary[offset: offset + 4])
        offset += 4

        return {
            'E1': e1,
            'E2': e2,
            'E3': e3,
            'E4': e4,

        }

    def struct_f(offset: int) -> dict:
        [k] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        [offset1] = struct.unpack('> I', binary[offset: offset + 4])
        s = '>' + str(k) + 'f'
        f1 = list(struct.unpack(s, binary[offset1: offset1 + 4 * k]))
        offset += 4
        [f2] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2

        return {
            'F1': f1,
            'F2': f2,

        }

    return struct_a(4)



