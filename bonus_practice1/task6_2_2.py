from unittest import TestCase

from task6_2_1 import fast_pow


class Test(TestCase):
    def fast_pow_test():
        for x in range(101):
            for y in range(101):
                assert fast_pow(x, y) == x ** y
        print("success")
    fast_pow_test()


