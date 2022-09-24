def valid_date(date):
    if date == "":
        return False
    date_list = date.split("-")
    if len(date_list) != 3:
        return False
    if int(date_list[0]) < 1 or int(date_list[0]) > 12:
        return False
    if int(date_list[0]) in [1, 3, 5, 7, 8, 10, 12]:
        if int(date_list[1]) < 1 or int(date_list[1]) > 31:
            return False
    elif int(date_list[0]) in [4, 6, 9, 11]:
        if int(date_list[1]) < 1 or int(date_list[1]) > 30:
            return False
    elif int(date_list[0]) == 2:
        if int(date_list[1]) < 1 or int(date_list[1]) > 29:
            return False
    if int(date_list[2]) < 1:
        return False
    return True
def check(candidate):

    # Check some simple cases
    assert candidate('03-11-2000') == True

    assert candidate('15-01-2012') == False

    assert candidate('04-0-2040') == False

    assert candidate('06-04-2020') == True

    assert candidate('01-01-2007') == True

    assert candidate('03-32-2011') == False

    assert candidate('') == False

    assert candidate('04-31-3000') == False

    assert candidate('06-06-2005') == True

    assert candidate('21-31-2000') == False

    assert candidate('04-12-2003') == True

    assert candidate('04122003') == False

    assert candidate('20030412') == False

    assert candidate('2003-04') == False

    assert candidate('2003-04-12') == False

    assert candidate('04-2003') == False

check(valid_date)