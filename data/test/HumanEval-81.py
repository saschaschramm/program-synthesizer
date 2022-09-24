def numerical_letter_grade(grades):
    grades_list = []
    for grade in grades:
        if grade >= 4.0:
            grades_list.append('A+')
        elif grade >= 3.7:
            grades_list.append('A')
        elif grade >= 3.3:
            grades_list.append('A-')
        elif grade >= 3.0:
            grades_list.append('B+')
        elif grade >= 2.7:
            grades_list.append('B')
        elif grade >= 2.3:
            grades_list.append('B-')
        elif grade >= 2.0:
            grades_list.append('C+')
        elif grade >= 1.7:
            grades_list.append('C')
        elif grade >= 1.3:
            grades_list.append('C-')
        elif grade >= 1.0:
            grades_list.append('D+')
        elif grade >= 0.7:
            grades_list.append('D')
        elif grade >= 0.0:
            grades_list.append('D-')
        else:
            grades_list.append('E')
    return grades_list
def check(candidate):

    # Check some simple cases
    assert candidate([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    assert candidate([1.2]) == ['D+']
    assert candidate([0.5]) == ['D-']
    assert candidate([0.0]) == ['E']
    assert candidate([1, 0.3, 1.5, 2.8, 3.3]) == ['D', 'D-', 'C-', 'B', 'B+']
    assert candidate([0, 0.7]) == ['E', 'D-']

    # Check some edge cases that are easy to work out by hand.
    assert True


check(numerical_letter_grade)