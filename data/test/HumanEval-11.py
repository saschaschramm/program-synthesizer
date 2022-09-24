from typing import List


def string_xor(a: str, b: str) -> str:
    return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

check(string_xor)