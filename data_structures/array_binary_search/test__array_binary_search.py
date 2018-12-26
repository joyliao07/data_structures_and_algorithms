"""To test the functions in array_binary_search.py."""
from .array_binary_search import BinarySearch


def test_BinarySearch_Valid_Input():
    """THIS IS TO TEST BINARYSEARCH WITH VALID INPUT."""
    input = [1, 2, 3, 4]
    value = 2
    expected = 1
    assert BinarySearch(input, value) == expected


def test_BinarySearch_Invalid_Input():
    """THIS IS TO TEST BINARYSEARCH WITH AN INVALID INPUT LIST."""
    input = 'a string'
    value = 2
    expected = 'TypeError'
    assert BinarySearch(input, value) == expected


def test_BinarySearch_Value_Not_Found_In_List():
    """TO TEST BINARYSEARCH WHEN VALUE IS NOT IN THE LIST."""
    input = [1, 2, 3, 4]
    value = 5
    expected = -1
    assert BinarySearch(input, value) == expected
