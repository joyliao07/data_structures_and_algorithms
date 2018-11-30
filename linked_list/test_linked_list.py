from .linked_list import LinkedList
import pytest


@pytest.fixture
def empty_ll():
    return LinkedList()


@pytest.fixture
def small_ll():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


@pytest.fixture
def random_ll():
    from random import randint
    ll = LinkedList()
    for num in range(10):
        ll.insert(randint(1, 100))
    return ll


def test_linkedlist_exist():
    assert LinkedList


def test_ll_str_method(empty_ll):
    assert str(empty_ll) == f'Linked List: Head val is: {empty_ll.head}'


def test_size_of_empty_ll(empty_ll):
    assert len(empty_ll) == 0


def test_small_fixture_has_size_of_4(small_ll):
    assert len(small_ll) == 4


def test_insert_new_node_into_empty_list(empty_ll):
    assert empty_ll.head is None
    empty_ll.insert(2)  ##############
    assert empty_ll.head.val == 2


def test_random_ll(random_ll):
    assert len(random_ll) == 10


def test_iterable_as_argument():
    ll = LinkedList([1, 2, 3, 4])
    assert ll.head.val == 4
    assert len(ll) == 4


def test_includes_work(small_ll):
    test = small_ll.includes(3)
    assert test


def test_includes_return_false(small_ll):
    test = small_ll.includes(11)
    assert test is False



