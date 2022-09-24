def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return greatest_common_divisor(a % b, b)
    else:
        return greatest_common_divisor(a, b % a)


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3, 7) == 1
    assert candidate(10, 15) == 5
    assert candidate(49, 14) == 7
    assert candidate(144, 60) == 12

check(greatest_common_divisor)