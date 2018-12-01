"""This module will test result of the LinkedList class and their methods."""
from .linked_list import LinkedList
import pytest


@pytest.fixture
def empty_ll():
    """To create an empty list for testing purpose."""
    return LinkedList()


@pytest.fixture
def small_ll():
    """To create a small list for testing purpose."""
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


@pytest.fixture
def random_ll():
    """To create a random list for testing purpose."""
    from random import randint
    ll = LinkedList()
    for num in range(10):
        ll.insert(randint(1, 100))
    return ll


def test_linkedlist_exist():
    """To test that the class LinkedList exists."""
    assert LinkedList


def test_ll_str_method(empty_ll):
    """To test the output of str method."""
    assert str(empty_ll) == f'Linked List: Head val is: {empty_ll.head}'


def test_size_of_empty_ll(empty_ll):
    """To test the size of the empty list created."""
    assert len(empty_ll) == 0


def test_small_fixture_has_size_of_4(small_ll):
    """To test the size of the small list created."""
    assert len(small_ll) == 4


def test_insert_new_node_into_empty_list(empty_ll):
    """To test the result of the insert function with a valid input."""
    assert empty_ll.head is None
    empty_ll.insert(2)
    assert empty_ll.head.val == 2


def test_insert_new_node_into_empty_input(empty_ll):
    """To test the result of the insert function with an empty input."""
    assert empty_ll.head is None
    empty_ll.insert('')
    assert empty_ll.head.val == ''


def test_random_ll(random_ll):
    """To test the length of the output of the random_ll function."""
    assert len(random_ll) == 10


def test_iterable_as_argument():
    """To test the output of iterable as argument."""
    ll = LinkedList([1, 2, 3, 4])
    assert ll.head.val == 4
    assert len(ll) == 4


def test_includes_work(small_ll):
    """To test includes method when the linked list does include the desired value."""
    test = small_ll.includes(3)
    assert test


def test_includes_no_searched(small_ll):
    """To test includes method when the desired value is None."""
    missing = None
    test = small_ll.includes(missing)
    assert test is False


def test_includes_return_false(small_ll):
    """To test includes method when the linked list does not include the desired value."""
    test = small_ll.includes(11)
    assert test is False
