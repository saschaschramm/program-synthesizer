def largest_prime_factor(n: int):
    for i in range(2, n):
        if n % i == 0:
            return largest_prime_factor(n // i)
    return n


METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)