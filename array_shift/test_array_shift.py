def test_insertShiftArray_even_element_array():
    #THIS IS TO TEST INSERTSHIFTARRAY WITH AN INPUT LIST THAT HAS AN EVEN NUMBER OF ITEMS
    from .array_shift import insertShiftArray
    input = [1, 2, 3, 4]
    value = 7
    expected = [1, 2, 7, 3, 4]
    assert insertShiftArray(input, value) == expected


def test_insertShiftArray_odd_element_array():
    #THIS IS TO TEST INSERTSHIFTARRAY WITH AN INPUT LIST THAT HAS AN ODD NUMBER OF ITEMS
    from .array_shift import insertShiftArray
    input = [1, 2, 3, 4, 5]
    value = 7
    expected = [1, 2, 3, 7, 4, 5]
    assert insertShiftArray(input, value) == expected


def test_insertShiftArray_type_error():
    #THIS IS TO TEST INSERTSHIFTARRAY WITH AN INPUT THAT IS NOT A LIST
    from .array_shift import insertShiftArray
    input = 'wrong type'
    value = 7
    expected = 'TypeError'
    assert insertShiftArray(input, value) == expected

