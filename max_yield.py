import doctest
import math

def allowed_to_be_added(index, already_added):
    for i in already_added:
        if math.fabs(i - index) == 1 or i - index == 0:
            return False
    return True

def max_yield(arr):
    """
    Description

    >>> max_yield([1])
    (1, [1])
    >>> max_yield([0])
    (0, [0])
    >>> max_yield([206, 140, 300, 52, 107])
    (613, [206, 'x', 300, 'x', 107])
    >>> max_yield([147, 206, 52, 240, 300])
    (506, ['x', 206, 'x', 'x', 300])
    >>> max_yield([206, 0, 230, 240, 0, 10000])
    (10446, [206, 'x', 'x', 240, 'x', 10000])
    >>> max_yield([-1])
    Incorrect data is given: must be numbers >= 0
    >>> max_yield(['garbage'])
    Incorrect data is given: must be numbers >= 0
    >>> max_yield([x for x in range(500)])[0]
    62500
    """

    #data validation
    for i in arr:
        e = ValueError("Incorrect data is given: must be numbers >= 0")
        try:
            if not int(i) >= 0:
                raise e
        except Exception:
            print(e)
            return

    first_arr = arr.copy()
    arr.sort()
    arr.reverse()
    result = 0
    already_added = []
    for i in arr:
        if allowed_to_be_added(first_arr.index(i), already_added):
            result += i
            already_added.append(first_arr.index(i))
        else:
            first_arr[first_arr.index(i)] = 'x'
    # print(arr)
    return result, first_arr

if __name__ == "__main__":
    doctest.testmod()