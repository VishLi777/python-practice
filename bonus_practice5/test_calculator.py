import random
import calculator

def test_calculator():
    for _ in range(10000):
        start(gen())


def start(s):
    try:
        return calculator.calculate(s)
    except:
        pass


def gen():
    a = '+-*/'
    b = '()'
    return ' '.join(
        [' '.join(
            [''.join(
                [str(random.choice(range(9)))
                 for _ in range(random.choice(range(1, 5)))]),
                random.choice(a), random.choice(b)])
            for _ in range(random.choice(range(5)))])