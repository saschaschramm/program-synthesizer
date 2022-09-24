from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers) - 1):
        result.append(numbers[i])
        result.append(delimeter)
    result.append(numbers[-1])
    return result


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([], 7) == []
    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]
    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]

check(intersperse)