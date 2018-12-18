"""This module will test result of class BST and its methods."""
from ..binary_search_tree import NodeTree, NodeQueue, Queue, BST
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
    short = NodeTree('1')
    assert str(short) == '1'


def test_repr_method_for_node():
    """To test the output of repr method."""
    short = NodeTree('1')
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


def test_in_order_with_empty_input():
    """To test in_order method with an empty tree."""
    tree_new = BST()
    with pytest.raises(TypeError) as err:
        tree_new.in_order_traversal(tree_new.root)
        assert str(err.value) == (f'There is no node to traverse.')


def test_in_order_with_valid_input(capsys):
    """To test in_order method with valid input."""
    tree_new = BST([10, 12, 11, 15, 20, 17])
    tree_new.in_order_traversal(tree_new.root)
    captured = capsys.readouterr()
    assert captured.out == '10\n11\n12\n15\n17\n20\n'


def test_in_order_with_valid_input_edge_case(capsys):
    """To test in_order method with valid input."""
    tree_new = BST([10])
    tree_new.in_order_traversal(tree_new.root)
    captured = capsys.readouterr()
    assert captured.out == '10\n'


def test_pre_order_with_empty_input():
    """To test pre_order method with an empty tree."""
    tree_new = BST()
    with pytest.raises(TypeError) as err:
        tree_new.pre_order_traversal(tree_new.root)
        assert str(err.value) == (f'There is no node to traverse.')


def test_pre_order_with_valid_input(capsys):
    """To test pre_order method with valid input."""
    tree_new = BST([10, 12, 11, 15, 20, 17])
    tree_new.pre_order_traversal(tree_new.root)
    captured = capsys.readouterr()
    assert captured.out == '10\n12\n11\n15\n20\n17\n'


def test_pre_order_with_valid_input_edge_case(capsys):
    """To test pre_order method with valid input."""
    tree_new = BST([10])
    tree_new.pre_order_traversal(tree_new.root)
    captured = capsys.readouterr()
    assert captured.out == '10\n'


def test_post_order_with_empty_input():
    """To test post_order method with an empty tree."""
    tree_new = BST()
    with pytest.raises(TypeError) as err:
        tree_new.post_order_traversal(tree_new.root)
        assert str(err.value) == (f'There is no node to traverse.')


def test_post_order_with_valid_input(capsys):
    """To test post_order method with valid input."""
    tree_new = BST([10, 12, 11, 15, 20, 17])
    tree_new.post_order_traversal(tree_new.root)
    captured = capsys.readouterr()
    assert captured.out == '11\n17\n20\n15\n12\n10\n'


def test_post_order_with_valid_input_edge_case(capsys):
    """To test post_order method with valid input."""
    tree_new = BST([10])
    tree_new.post_order_traversal(tree_new.root)
    captured = capsys.readouterr()
    assert captured.out == '10\n'


def test_breadth_first_with_valid_input(capsys):
    """To test breadth_first method with valid input."""
    tree_new = BST([10, 12, 11, 15, 20, 17])
    tree_new.breadth_first(tree_new.root)
    captured = capsys.readouterr()
    assert captured.out == '10\n12\n11\n15\n20\n17\n'


def test_breadth_first_with_valid_input_2(capsys):
    """To test breadth_first method with valid input."""
    tree_new = BST([40, 15, 47, 20, 30, 50, 65])
    tree_new.breadth_first(tree_new.root)
    captured = capsys.readouterr()
    assert captured.out == '40\n15\n47\n20\n50\n30\n65\n'


def test_breadth_first_with_empty_input():
    """To test breadth_first method with an empty tree."""
    tree_new = BST()
    with pytest.raises(TypeError) as err:
        tree_new.breadth_first(tree_new.root)
        assert str(err.value) == (f'There is no node to traverse.')


def test_breadth_first_with_valid_input_edge_case(capsys):
    """To test breadth_first method with valid input."""
    tree_new = BST([10])
    tree_new.breadth_first(tree_new.root)
    captured = capsys.readouterr()
    assert captured.out == '10\n'
