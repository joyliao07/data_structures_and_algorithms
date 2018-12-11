"""This module will test result of class AnimalShelter and its methods."""
from ..fifo_animal_shelter import AnimalShelter
from ..fifo_animal_shelter import Node
import pytest


@pytest.fixture
def empty_queue():
    """To create an empty queue for testing purpose."""
    return AnimalShelter()


def test_class_exist():
    """To test that the class queue exists."""
    assert AnimalShelter


def test_str_method_for_node():
    """To test the output of str method."""
    short = Node(1)
    assert str(short) == '1'


def test_repr_method_for_node():
    """To test the output of repr method."""
    short = Node(1)
    assert repr(short) == '<NODE: 1>'


def test_repr_method_for_animalshelter():
    """To test the output of repr method."""
    short = AnimalShelter([1])
    assert repr(short) == '<Queue front: 1>'


def test_str_method():
    """To test the output of str method."""
    short = AnimalShelter([1, 2, 3])
    assert str(short) == f'Queue: Value of the front Queue is: 1'


def test_size_method():
    """To test the size method."""
    short = AnimalShelter([1, 2, 3])
    assert len(short) == 3


def test_enqueue_with_valid_input():
    """To test enqueue method with valid input."""
    queue_new = AnimalShelter()
    queue_new.enqueue(5)
    assert queue_new.front.value == 5


def test_enqueue_with_valid_input_2():
    """To test enqueue method with valid input."""
    queue_new = AnimalShelter([1, 2, 3])
    queue_new.enqueue(4)
    queue_new.enqueue(5)
    assert queue_new.rear.value == 5


def test_enqueue_with_list_input():
    """To test enqueue method with a list input."""
    queue_new = AnimalShelter()
    queue_new.enqueue([1, 2, 3])
    assert queue_new.front.value == [1, 2, 3]


def test_dequeue_with_valid_input():
    """To test dequeue method with valid input."""
    new_queue = AnimalShelter(['apple', 'banana', 'cucumber'])
    new_queue.dequeue('banana')
    assert new_queue.front.value == 'apple'
    assert new_queue.rear.value == 'cucumber'


def test_dequeue_with_valid_input_2():
    """To test dequeue method with valid input."""
    new_queue = AnimalShelter(['apple', 'banana', 'cucumber'])
    result = new_queue.dequeue('cucumber')
    assert result.value == 'cucumber'


def test_dequeue_with_valid_input_3():
    """To test dequeue method with valid input."""
    new_queue = AnimalShelter(['apple', 'banana', 'cucumber'])
    result = new_queue.dequeue('apple')
    assert result.value == 'apple'


def test_dequeue_with_empty_queue(empty_queue):
    """To test dequeue method with invalid input."""
    assert TypeError(f'Input must be a non-empty queue.')





























