"""Write BinarySearch function that finds the position of a value in a list."""

lst = [1, 2, 3, 4, 5]
val = 10


def BinarySearch(lst, val):
    """
    Given a list and a value, return the position of the value in the list.

    Return -1 if the value is not in the list.
    """
    status = False
    if isinstance(lst, list) is False:
        print('TypeError')
        return('TypeError')
    for n in range(len(lst)):
        if lst[n] == val:
            status = True
            print(n)
            return(n)
    if status is False:
        print(-1)
        return(-1)


BinarySearch(lst, val)
