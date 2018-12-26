"""This module will test result of class Stack and its methods."""
from .queue import Queue
import pytest


@pytest.fixture
def empty_queue():
    """To create an empty queue for testing purpose."""
    return Queue()


def test_queue_exist():
    """To test that the class queue exists."""
    assert Queue


def test_str_method():
    """To test the output of str method."""
    short = Queue([1, 2, 3])
    assert str(short) == f'Queue: Value of the front Queue is: 1'


def test_size_method():
    """To test the size method."""
    short = Queue([1, 2, 3])
    assert len(short) == 3


def test_enqueue_with_valid_input():
    """To test enqueue method with valid input."""
    queue_new = Queue()
    queue_new.enqueue(5)
    assert queue_new.front.value == 5


def test_enqueue_with_valid_input_2():
    """To test enqueue method with valid input."""
    queue_new = Queue([1, 2, 3])
    queue_new.enqueue(4)
    queue_new.enqueue(5)
    assert queue_new.rear.value == 5


def test_enqueue_with_list_input():
    """To test enqueue method with a list input."""
    queue_new = Queue()
    queue_new.enqueue([1, 2, 3])
    assert queue_new.front.value == [1, 2, 3]


def test_dequeue_with_valid_input():
    """To test dequeue method with valid input."""
    new_queue = Queue(['apple', 'banana', 'cucumber'])
    new_queue.dequeue()
    assert new_queue.front.value == 'banana'
    assert new_queue.rear.value == 'cucumber'


def test_dequeue_with_valid_input():
    """To test dequeue method with valid input."""
    new_queue = Queue(['apple', 'banana', 'cucumber'])
    result = new_queue.dequeue()
    assert result.value == 'apple'
    assert result.next_node is None


def test_dequeue_with_empty_queue(empty_queue):
    """To test dequeue method with invalid input."""
    assert empty_queue.dequeue() == f'Input must be a non-empty queue.'


def test_peek_with_valid_input():
    """To test peek method with invalid input."""
    new_queue = Queue(['apple', 'banana', 'cucumber'])
    assert new_queue.peek() == 'apple'


def test_peek_with_valid_input_2():
    """To test peek method with invalid input."""
    new_queue = Queue(['apple', 'banana', 'cucumber'])
    new_queue.dequeue()
    assert new_queue.peek() == 'banana'


def test_peek_with_empty_queue(empty_queue):
    """To test peek method with invalid input."""
    assert empty_queue.peek() == f'Input must be a non-empty queue.'










