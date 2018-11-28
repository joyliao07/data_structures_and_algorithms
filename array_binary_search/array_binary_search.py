
lst = [1, 2, 3, 4, 5]
val = 'typing'


def BinarySearch(lst, val):
    """
    Given a list and a value, return the position of the value in the list. Return -1 if the value is not in the list. 
    Input -> be a list and a value
    Output -> be a number as the index position or -1.
    """
    status = False
    if isinstance(lst, list):
        print('here is the type err ')
        return(TypeError)
    for n in range(len(lst)):
        if lst[n] == val:
            status = True
            print(n)
            return(n)
    if status is not True:
        print(-1)
        return(-1)




BinarySearch(lst, val)


