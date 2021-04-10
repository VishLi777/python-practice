from unittest import TestCase

from task6_1_1 import fast_mul


class Test(TestCase):
    def fast_mul_test():
        for x in range(101):
            for y in range(101):
                assert fast_mul(x, y) == x * y
        print("success")
    fast_mul_test()

