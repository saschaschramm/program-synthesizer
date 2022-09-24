def total_match(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return []
    elif len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    else:
        total_lst1 = 0
        total_lst2 = 0
        for i in lst1:
            total_lst1 += len(i)
        for i in lst2:
            total_lst2 += len(i)
        if total_lst1 < total_lst2:
            return lst1
        elif total_lst1 > total_lst2:
            return lst2
        else:
            return lst1
def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([], []) == []
    assert candidate(['hi', 'admin'], ['hi', 'hi']) == ['hi', 'hi']
    assert candidate(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) == ['hi', 'admin']
    assert candidate(['4'], ['1', '2', '3', '4', '5']) == ['4']
    assert candidate(['hi', 'admin'], ['hI', 'Hi']) == ['hI', 'Hi']
    assert candidate(['hi', 'admin'], ['hI', 'hi', 'hi']) == ['hI', 'hi', 'hi']
    assert candidate(['hi', 'admin'], ['hI', 'hi', 'hii']) == ['hi', 'admin']


    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([], ['this']) == []
    assert candidate(['this'], []) == []


check(total_match)