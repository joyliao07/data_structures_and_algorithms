"""This module will contain class Hash and its related methods."""
from ..left_join import Hash
import pytest


def test_class_exist():
    """To test that the class Graph exists."""
    assert Hash


def test_str_method_empty():
    """To test the output of str method."""
    h = Hash()
    assert str(h) == 'Hash table length is 0'


def test_repr_method_empty():
    """To test the output of repr method."""
    h = Hash()
    assert repr(h) == '<Hash table list: []>'


def test_add_hash_with_valid_value():
    """To test add_hash method with valid input."""
    h = Hash()
    h.add_hash(["apple", 300])
    assert repr(h) == "<Hash table list: [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [['apple', 300]]]>"


def test_add_hash_with_valid_value_2():
    """To test add_hash method with valid input."""
    h = Hash([["apple", 300], ['banana', 15]])
    assert repr(h) == "<Hash table list: [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [['apple', 300]], [], [], [], [], [], [], [['banana', 15]]]>"


def test_add_hash_with_valid_value_3():
    """To test add_hash method with valid input."""
    h = Hash([["apple", 300], ['banana', 15], ['baaann', 30]])
    assert repr(h) == "<Hash table list: [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [['apple', 300]], [], [], [], [], [], [], [['banana', 15], ['baaann', 30]]]>"


def test_retrieve_val_with_empty_value():
    """To test retrieve_val method with empty input."""
    h = Hash([["apple", 300], ['banana', 15]])
    with pytest.raises(TypeError) as err:
        h.retrieve_val(None)
    assert str(err.value) == 'No key to look for.'


def test_retrieve_val_with_valid_value_1():
    """To test retrieve_val method with valid input."""
    h = Hash([["apple", 300], ['banana', 15]])
    assert h.retrieve_val('apple') == 300


def test_retrieve_val_with_valid_value_2():
    """To test retrieve_val method with valid input."""
    h = Hash([["apple", 300], ['banana', 15]])
    h.add_hash(['cranberry', 45])
    assert h.retrieve_val('cranberry') == 45


def test_retrieve_val_with_value_not_exist():
    """To test retrieve_val method with no matching key."""
    h = Hash([["apple", 300], ['banana', 15]])
    assert h.retrieve_val('cranberry') == 'No matching key is found.'


def test_left_join_with_valid_value():
    """To test left_join method with valid input."""
    h1 = Hash([["apple", '3 apples from bucket 1'], ['banana', '4 bananas from bucket 1']])
    h2 = Hash([["apple", '5 apples from bucket 2'], ['banana', '2 bananas from bucket 2']])
    assert h1.left_join(h2) == [['apple', '3 apples from bucket 1', '5 apples from bucket 2'], ['banana', '4 bananas from bucket 1', '2 bananas from bucket 2']]


def test_left_join_with_some_value_not_in_h2():
    """To test left_join method with valid input."""
    h1 = Hash([["apple", '3 apples from bucket 1'], ['banana', '4 bananas from bucket 1'], ['cranberries', '20 cranberries from bucket 1']])
    h2 = Hash([["apple", '5 apples from bucket 2'], ['banana', '2 bananas from bucket 2']])
    assert h1.left_join(h2) == [['apple', '3 apples from bucket 1', '5 apples from bucket 2'], ['banana', '4 bananas from bucket 1', '2 bananas from bucket 2'], ['cranberries', '20 cranberries from bucket 1', 'Null']]


def test_left_join_with_missing_key():
    """To test left_join method with valid input."""
    h1 = Hash()
    h2 = Hash([["apple", '5 apples from bucket 2'], ['banana', '2 bananas from bucket 2']])
    with pytest.raises(TypeError) as err:
        h1.left_join(h2)
    assert str(err.value) == 'No key to look for.'
