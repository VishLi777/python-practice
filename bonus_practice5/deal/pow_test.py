import deal

from pow import pow2

@deal.cases(pow2)
def test_div(case: deal.TestCase) -> None:
    case()

# pytest deal/test_pow.py