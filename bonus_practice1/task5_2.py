from unittest import TestCase
from task5_1 import naive_mul


class Test(TestCase):
    def naive_mul_test(self):
        for i in range(100):
            for j in range(100):
                assert naive_mul(i, j) == i * j