num = [1, 2, 3, 4, 5]
value = 7


def insertShiftArray(num, value):
    #DOC: THE FUNCTION THAT TAKES IN AN ARRAY AND A VALUE, INSERT THE VALUE IN THE MIDDLE OF THE ARRAY, AND RETURN THE NEW ARRAY
    new = []
    if len(num) % 2 == 0:
        new = num[0 : len(num)//2]
        new.append(value)
        new = new + num[len(num)//2:]
        print(new)
    else:
        new = num[0 : len(num)//2 + 1]
        new.append(value)
        new = new + num[len(num)//2 + 1:]
        print(new)


insertShiftArray(num, value)









