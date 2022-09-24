def sum_to_n(n: int):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


METADATA = {}


def check(candidate):
    assert candidate(1) == 1
    assert candidate(6) == 21
    assert candidate(11) == 66
    assert candidate(30) == 465
    assert candidate(100) == 5050


check(sum_to_n)