def fib4(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    a = 0
    b = 0
    c = 2
    d = 0
    for i in range(4, n+1):
        e = a + b + c + d
        a = b
        b = c
        c = d
        d = e
    return d


METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)