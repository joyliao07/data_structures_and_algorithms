"""Write BinarySearch function that finds the position of a value in a list."""

lst = [1, 2, 3, 4, 5]
val = 1


def BinarySearch(lst, val):
    """
    Given a list and a value, return the position of the value in the list.

    Return -1 if the value is not in the list.
    """
    if isinstance(lst, list) is False:
        print('TypeError')
        return('TypeError')
    
    min = 0
    # Minus-one because max will be used to indicate the index number
    max = len(lst) - 1
    
    while True:
        if max < min:
            print(-1)
            return -1
        m = (min + max) // 2
        if lst[m] < val:
            min = m + 1
            # Plus-one so the function won't fall into a constant while loop
        elif lst[m] > val:
            max = m - 1
            # Minus-one so the function won't fall into a constant while loop
        elif lst[m] == val:
            print(m)
            return m

BinarySearch(lst, val)
