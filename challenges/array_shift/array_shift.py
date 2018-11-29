"""This module has insertShiftArray function."""


def insertShiftArray(num, value):
    """
    TO TAKE IN AN ARRAY AND A VALUE, INSERT VALUE IN THE MIDDLE.

    AND RETURN THE NEW ARRAY
    """
    if type(num) is not list:
        print('TypeError')
        return('TypeError')
    elif len(num) % 2 == 0:
        new = num[0:len(num)//2]
        new.append(value)
        new = new + num[len(num)//2:]
        print(new)
        return(new)
    else:
        new = num[0:len(num)//2 + 1]
        new.append(value)
        new = new + num[len(num)//2 + 1:]
        print(new)
        return(new)
