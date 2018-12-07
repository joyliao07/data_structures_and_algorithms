"""This module will test result of class Stack and its methods."""
from .stack import Stack
import pytest


def test_stack_exist():
    """To test that the class Stack exists."""
    assert Stack


def test_str_method():
    """To test the output of str method."""
    short = Stack([1, 2, 3])
    assert str(short) == f'Stack: Value of the top stack is: 3'


def test_size_method():
    """To test the size method."""
    short = Stack([1, 2, 3])
    assert len(short) == 3


def test_push_with_valid_input():
    """To test push method with valid input."""
    stack_new = Stack()
    stack_new.push(5)
    assert stack_new.top.value == 5


def test_push_with_list_input():
    """To test push method with a list input."""
    stack_new = Stack()
    stack_new.push([1, 2, 3])
    assert stack_new.top.value == [1, 2, 3]


def test_pop_with_valid_input():
    """To test pop method with valid input."""
    stack_new = Stack([1, 2, 3])
    stack_new.pop()
    assert stack_new.top.value == 2


def test_pop_with_empty_stack():
    """To test pop method with invalid input."""
    stack_new = Stack()
    result = stack_new.pop()
    assert result == f'Input stack cannot be empty.'


def test_peek_with_valid_input():
    """To test peek method with valid input."""
    stack_new = Stack([1, 2, 3])
    assert stack_new.peek() == 3


def test_peek_with_empty_stack():
    """To test peek method with invalid input."""
    stack_new = Stack()
    assert stack_new.peek() == f'Input must be a non-empty stack.'
