def get_odd_collatz(n):
    if n == 1:
        return [1]
    else:
        collatz = [n]
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            collatz.append(n)
        return sorted([x for x in collatz if x % 2 == 1])
def check(candidate):

    # Check some simple cases
    assert candidate(14) == [1, 5, 7, 11, 13, 17]
    assert candidate(5) == [1, 5]
    assert candidate(12) == [1, 3, 5], "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1) == [1], "This prints if this assert fails 2 (also good for debugging!)"


check(get_odd_collatz)