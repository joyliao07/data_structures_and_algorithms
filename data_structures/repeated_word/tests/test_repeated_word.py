"""This module will contain class Hash and its related methods."""
from ..repeated_word import Hash
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
    """To test retrieve_val method with valid input."""
    h = Hash([["apple", 300], ['banana', 15]])
    assert h.retrieve_val('cranberry') == 'No matching key is found.'


def test_add_word_with_valid_value_1():
    """To test add_word method with valid input."""
    h = Hash()
    h.add_word(['apple', None])
    assert str(h) == 'Hash table length is 53'


def test_add_word_with_empty_key():
    """To test add_word method with an empty key."""
    h = Hash()
    with pytest.raises(TypeError) as err:
        h.add_word([None, None])
    assert str(err.value) == 'No word in the string.'


def test_paragraph_with_empty_string():
    """To test paragraph method with an empty string."""
    h = Hash()
    with pytest.raises(TypeError) as err:
        h.paragraph('')
    assert str(err.value) == 'No word in the string.'


def test_paragraph_with_repeated_word(capsys):
    """To test paragraph method with repeated word in a string."""
    h = Hash()
    string = "Every day is a good day is a wonderful day."
    h.paragraph(string)
    captured = capsys.readouterr()
    assert captured.out == 'day\n'


def test_paragraph_with_non_string():
    """To test paragraph method with a non-string."""
    h = Hash()
    string = ['abc', None]
    with pytest.raises(TypeError) as err:
        h.paragraph(string)
    assert str(err.value) == 'Input is not a string.'
