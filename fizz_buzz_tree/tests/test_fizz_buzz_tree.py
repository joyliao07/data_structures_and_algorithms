"""This module will test result of fizz_buzz_tree and its methods."""
from ..fizz_buzz_tree import Node, BST
import pytest


@pytest.fixture
def empty_queue():
    """To create an empty queue for testing purpose."""
    return BST()


def test_class_exist():
    """To test that the class queue exists."""
    assert BST


def test_str_method_for_node():
    """To test the output of str method."""
    short = Node('1')
    assert str(short) == '1'


def test_repr_method_for_node():
    """To test the output of repr method."""
    short = Node('1')
    assert repr(short) == '<NODE: 1>'


def test_repr_method_for_bst():
    """To test the output of repr method."""
    short = BST(['1'])
    assert repr(short) == '<BST root: 1>'


def test_str_method_for_bst():
    """To test the output of str method."""
    short = BST(['1', '2', '3'])
    assert str(short) == f'Value of the root Queue is: 1'


def test_add_node_with_valid_input_edge_case():
    """To test add_node method with valid input."""
    tree_new = BST()
    tree_new.add_node(1)
    assert tree_new.root.val == 1


def test_add_node_with_valid_input():
    """To test add_node method with valid input."""
    tree_new = BST([1, 2])
    tree_new.add_node(3)
    assert tree_new.root.val == 1


def test_add_node_with_valid_input_2():
    """To test add_node method with valid input."""
    tree_new = BST([100])
    tree_new.add_node(3)
    assert tree_new.root.val == 100


def test_fizz_buzz_tree_with_valid_input(capsys):
    """To test fizz_buzz_tree with a valid tree."""
    tree_new = BST([10, 12, 11, 15, 20, 17])
    tree_new.fizz_buzz_tree(tree_new.root)
    tree_new.in_order_traversal(tree_new.root)
    captured = capsys.readouterr()
    assert captured.out == (f'Buzz\n11\nFizz\nFizzBuzz\n17\nBuzz\n')


def test_fizz_buzz_tree_with_empty_input(capsys):
    """To test fizz_buzz_tree with an empty tree."""
    tree_new = BST()
    with pytest.raises(TypeError) as err:
        tree_new.fizz_buzz_tree(tree_new.root)
        assert str(err.value) == (f'There is no node to traverse.')


def test_fizz_buzz_tree_with_valid_input_edge_case(capsys):
    """To test fizz_buzz_tree with an one-node tree."""
    tree_new = BST([15])
    tree_new.fizz_buzz_tree(tree_new.root)
    tree_new.in_order_traversal(tree_new.root)
    captured = capsys.readouterr()
    assert captured.out == (f'FizzBuzz\n')
