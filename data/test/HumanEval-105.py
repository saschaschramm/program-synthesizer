def by_length(arr):
    arr = sorted(arr)
    arr = arr[::-1]
    result = []
    for i in arr:
        if i == 1:
            result.append("One")
        elif i == 2:
            result.append("Two")
        elif i == 3:
            result.append("Three")
        elif i == 4:
            result.append("Four")
        elif i == 5:
            result.append("Five")
        elif i == 6:
            result.append("Six")
        elif i == 7:
            result.append("Seven")
        elif i == 8:
            result.append("Eight")
        elif i == 9:
            result.append("Nine")
    return result
def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"], "Error"
    assert candidate([]) == [], "Error"
    assert candidate([1, -1 , 55]) == ['One'], "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([1, -1, 3, 2]) == ["Three", "Two", "One"]
    assert candidate([9, 4, 8]) == ["Nine", "Eight", "Four"]


check(by_length)