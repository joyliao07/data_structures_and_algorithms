"""This module will contain class Sort and its related methods."""
from ..merge_sort import Sort
import pytest


def test_class_exist():
    """To test that the class exists."""
    assert Sort


def test_str_method_empty():
    """To test the output of str method."""
    s = Sort()
    assert str(s) == 'Input list length is 0'


def test_str_method_with_list():
    """To test the output of str method."""
    s = Sort([3, 1, 2])
    assert str(s) == 'Input list length is 3'


def test_repr_method_empty():
    """To test the output of repr method."""
    s = Sort()
    assert repr(s) == '<Input list: []>'


def test_repr_method_with_list():
    """To test the output of repr method."""
    s = Sort([3, 1, 2])
    assert repr(s) == '<Input list: [3, 1, 2]>'


def test_sort_with_valid_value():
    """To test selection method with valid input."""
    s = Sort([3, 2, 7, 4, 6])
    result = s.selection()
    assert result == [2, 3, 4, 6, 7]


def test_sort_with_negative_value():
    """To test selection method with list containing negative value."""
    s = Sort([3, 2, 7, 4, -11, 6])
    result = s.selection()
    assert result == [-11, 2, 3, 4, 6, 7]


def test_sort_with_letter():
    """To test selection method with list containing a letter."""
    s = Sort([3, 2, 7, 4, -11, 6, 'a'])
    with pytest.raises(TypeError) as err:
        s.selection()
    assert str(err.value) == 'Items must be integers.'


def test_mergeSort_with_list():
    """To test mergeSort method with a list."""
    s = Sort([3, 2, 7, 4, -11, 6, 5, -15])
    s.mergeSort()
    assert s.lst == [-15, -11, 2, 3, 4, 5, 6, 7]


def test_mergeSort_with_letter():
    """To test mergeSort method with a list that contains a letter."""
    s = Sort([3, 2, 7, 4, -11, 6, 5, -15, 'l'])
    with pytest.raises(TypeError) as err:
        s.mergeSort()
    assert str(err.value) == 'Items must be integers.'
