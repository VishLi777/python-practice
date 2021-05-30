import angle


def twelve_test():
    assert angle.between(12, 00) == 0


# pytest mutmut/angle_test.py --cov=. --cov-branch
