"""This module will test result of the ll_merge."""
from .ll_merge import LinkedList
from .ll_merge import Node
from .ll_merge import ll_merge
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


def test_linkedlist_exist():
    """To test that the class LinkedList exists."""
    assert LinkedList


def test_small_fixture_has_size_of_4(small_ll):
    """To test the size of the small list created."""
    assert len(small_ll) == 4


def test_ll_merge_with_valid_inputs():
    """To test ll_merge() with valid inputs."""
    ll_A = LinkedList([1, 2, 3, 4, 5])
    ll_B = LinkedList(['A', 'B', 'C'])
    result = ll_merge(ll_A, ll_B)
    assert len(result) == 8
    assert type(result) == LinkedList


def test_ll_merge_with_one_empty_ll():
    """To test ll_merge() with one empty linked list."""
    ll_A = LinkedList([1, 2, 3])
    ll_B = LinkedList()
    result = ll_merge(ll_A, ll_B)
    assert len(result) == 3
    assert type(result) == LinkedList


def test_ll_merge_with_two_empty_ll():
    """To test ll_merge() with two empty ll."""
    ll_A = LinkedList()
    ll_B = LinkedList()
    result = ll_merge(ll_A, ll_B)
    assert len(result) == 0
    assert type(result) == LinkedList
