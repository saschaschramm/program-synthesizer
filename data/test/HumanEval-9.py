from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(max(numbers[:i + 1]))
    return result


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]

check(rolling_max)