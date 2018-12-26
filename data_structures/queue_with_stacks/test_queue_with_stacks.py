"""This module will test result of class PseudoQueue and its methods."""
from .queue_with_stacks import PseudoQueue
import pytest


def test_pseudoqueue_exit():
    """To test that the class PseudoQueue exists."""
    assert PseudoQueue


def test_pseudoqueue_create_a_pseudoqueue():
    """To test that the class PseudoQueue creates a pseudoqueue."""
    result = PseudoQueue()
    assert type(result) == PseudoQueue


def test_pseudoqueue_enqueue_empty():
    """To test enqueue return an empty stack."""
    result = PseudoQueue()
    result.enqueue(None)
    assert result.stack_1.top.value is None
    assert len(result.stack_1) == 1


def test_pseudoqueue_enqueue():
    """To test enqueue properly works with valid inputs."""
    result = PseudoQueue()
    result.enqueue('a')
    result.enqueue('b')
    result.enqueue('c')
    assert result.rear.value == 'c'
    assert len(result.stack_1) == 3


def test_dequeue():
    """To test dequeue properly works with valid inputs."""
    result = PseudoQueue()
    result.enqueue('a')
    result.enqueue('b')
    result.enqueue('c')
    result.dequeue()
    assert result.rear.value == 'c'
    assert len(result.stack_1) == 2


def test_dequeue_consecutively():
    """To test dequeue properly works consecutive times."""
    result = PseudoQueue()
    result.enqueue('a')
    result.enqueue('b')
    result.enqueue('c')
    result.dequeue()
    result.dequeue()
    assert result.rear.value == 'c'
    assert len(result.stack_1) == 1


def test_dequeue_with_empty_error():
    """To test dequeue with an empty self."""
    result = PseudoQueue()
    answer = result.dequeue()
    assert answer == f'Input stack cannot be empty.'
