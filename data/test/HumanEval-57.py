def monotonic(l: list):
    if len(l) == 1:
        return True
    if l[0] < l[1]:
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False
    else:
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                return False
    return True


METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10]) == True
    assert candidate([1, 2, 4, 20]) == True
    assert candidate([1, 20, 4, 10]) == False
    assert candidate([4, 1, 0, -10]) == True
    assert candidate([4, 1, 1, 0]) == True
    assert candidate([1, 2, 3, 2, 5, 60]) == False
    assert candidate([1, 2, 3, 4, 5, 60]) == True
    assert candidate([9, 9, 9, 9]) == True


check(monotonic)