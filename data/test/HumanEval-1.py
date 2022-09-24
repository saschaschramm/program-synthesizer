from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")
    paren_groups = []
    current_group = ""
    open_parens = 0
    for char in paren_string:
        if char == "(":
            open_parens += 1
        elif char == ")":
            open_parens -= 1
        current_group += char
        if open_parens == 0:
            paren_groups.append(current_group)
            current_group = ""
    return paren_groups


METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [
        '(()())', '((()))', '()', '((())()())'
    ]
    assert candidate('() (()) ((())) (((())))') == [
        '()', '(())', '((()))', '(((())))'
    ]
    assert candidate('(()(())((())))') == [
        '(()(())((())))'
    ]
    assert candidate('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

check(separate_paren_groups)