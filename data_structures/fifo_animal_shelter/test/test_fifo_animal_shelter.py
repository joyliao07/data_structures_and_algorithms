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
    short = Node('dog')
    assert str(short) == 'dog'


def test_repr_method_for_node():
    """To test the output of repr method."""
    short = Node('dog')
    assert repr(short) == '<NODE: dog>'


def test_repr_method_for_animalshelter():
    """To test the output of repr method."""
    short = AnimalShelter(['dog'])
    assert repr(short) == '<Queue front: dog>'


def test_str_method():
    """To test the output of str method."""
    short = AnimalShelter(['dog', 'cat', 'cat'])
    assert str(short) == f'Queue: Value of the front Queue is: dog'


def test_size_method():
    """To test the size method."""
    short = AnimalShelter(['dog', 'cat', 'cat'])
    assert len(short) == 3


def test_enqueue_with_valid_input():
    """To test enqueue method with valid input."""
    queue_new = AnimalShelter()
    queue_new.enqueue('dog')
    assert queue_new.front.value == 'dog'


def test_enqueue_with_valid_input_2():
    """To test enqueue method with valid input."""
    queue_new = AnimalShelter(['dog', 'dog', 'dog'])
    queue_new.enqueue('cat')
    queue_new.enqueue('cat')
    assert queue_new.rear.value == 'cat'


def test_enqueue_with_list_input():
    """To test enqueue method with a list input."""
    queue_new = AnimalShelter()
    with pytest.raises(TypeError) as excinfo:
        queue_new.enqueue(['cat', 'cat', 'cat'])
        assert str(excinfo.value) == (f'The input must be dog or cat.')


def test_dequeue_with_valid_input():
    """To test dequeue method with valid input."""
    new_queue = AnimalShelter(['cat', 'cat', 'dog'])
    new_queue.dequeue('dog')
    assert new_queue.front.value == 'cat'
    assert new_queue.rear.value == 'cat'


def test_dequeue_with_valid_input_3():
    """To test dequeue method with valid input."""
    new_queue = AnimalShelter(['cat', 'cat', 'dog'])
    result = new_queue.dequeue('cat')
    assert result.value == 'cat'


def test_dequeue_with_empty_queue(empty_queue):
    """To test dequeue method with invalid input."""
    assert TypeError(f'Input must be a non-empty queue.')

