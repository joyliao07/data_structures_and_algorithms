"""This module will contain class Graph and its related methods."""
from ..breadth_first import Graph
from .conftest import graph_empty, graph_one, graph_two
import pytest


def test_class_exist():
    """To test that the class Graph exists."""
    assert Graph


def test_str_method_empty(graph_empty):
    """To test the output of str method."""
    assert str(graph_empty) == "The list of vertices are: dict_keys([])"


def test_str_method(graph_one):
    """To test the output of str method."""
    assert str(graph_one) == "The list of vertices are: dict_keys(['A', 'B', 'C', 'D', 'E', 'F'])"


def test_repr_method_empty(graph_empty):
    """To test the output of repr method."""
    assert repr(graph_empty) == "<List of vertices: dict_keys([])>"


def test_repr_method(graph_two):
    """To test the output of repr method."""
    assert repr(graph_two) == "<List of vertices: dict_keys(['A', 'B', 'C', 'D', 'E', 'F', 'G'])>"


def test_len_method(graph_one):
    """To test the output of repr method."""
    assert len(graph_one) == 6


def test_len_method_2(graph_two):
    """To test the output of repr method."""
    assert len(graph_two) == 7


def test_len_method_empty(graph_empty):
    """To test the output of repr method."""
    assert len(graph_empty) == 0


def test_add_vert_with_valid_value(graph_empty):
    """To test add_vert method with valid input."""
    graph_empty.add_vert('ABC')
    assert repr(graph_empty) == "<List of vertices: dict_keys(['ABC'])>"


def test_add_vert_with_empty_value(graph_one):
    """To test add_vert method with valid input."""
    graph_one.add_vert('')
    assert repr(graph_one) == "<List of vertices: dict_keys(['A', 'B', 'C', 'D', 'E', 'F', ''])>"


def test_add_vert_with_list_value(graph_one):
    """To test add_vert method with invalid input of a list."""
    with pytest.raises(KeyError) as err:
        graph_one.add_vert([1, 2])
        assert str(err.value) == 'Val must be a string or a number.'


def test_add_vert_with_dict_value(graph_one):
    """To test add_vert method with invalid input of a dictionary."""
    with pytest.raises(KeyError) as err:
        graph_one.add_vert({})
        assert str(err.value) == 'Val must be a string or a number.'


def test_has_vert_with_value_not_exist(graph_empty):
    """To test has_vert method with value that does not exist."""
    assert graph_empty.has_vert('ABC') is False


def test_has_vert_with_value_that_exist(graph_one):
    """To test has_vert method with value that does not exist."""
    assert graph_one.has_vert('A') is True


def test_has_vert_with_value_not_exist(graph_empty):
    """To test has_vert method with value that does not exist."""
    assert graph_empty.has_vert(None) is False


def test_add_edge_with_valid_values(graph_one):
    """To test add_edge method with valid input."""
    graph_one.add_edge('A', 'C', 100)
    assert graph_one.gdict['A'] == {'B': 10, 'C': 100}


def test_add_edge_with_vert_not_exist(graph_one):
    """To test add_edge method with valid input."""
    with pytest.raises(KeyError) as err:
        graph_one.add_edge('Abc', 'C', 100)
        assert str(err.value) == "The vert does not exist."


def test_add_edge_with_empty_val(graph_one):
    """To test add_edge method with valid input."""
    graph_one.add_edge('A', 'C', None)
    assert graph_one.gdict['A'] == {'B': 10, 'C': None}


def test_get_neighbors_with_valid_values(graph_one):
    """To test get_neighbors method with valid input."""
    graph_one.get_neighbors('A')
    assert graph_one.gdict['A'] == {'B': 10}


def test_get_neighbors_with_valid_not_exist(graph_one):
    """To test get_neighbors method with valid input."""
    with pytest.raises(KeyError) as err:
        graph_one.get_neighbors('Abc')
        assert str(err.value) == "The vert does not exist."


def test_breadth_first_graph_one(graph_one, capsys):
    """To test breadth_first method with valid input."""
    graph_one.breadth_first('A')
    captured = capsys.readouterr()
    assert captured.out == 'A\nB\nD\nC\nE\nF\n'


def test_breadth_first_graph_two(graph_two, capsys):
    """To test breadth_first method with valid input."""
    graph_two.breadth_first('A')
    captured = capsys.readouterr()
    assert captured.out == 'A\nB\nC\nD\nE\nF\nG\n'


def test_breadth_first_empty(graph_empty, capsys):
    """To test breadth_first method with empty input."""
    with pytest.raises(TypeError) as err:
        graph_empty.breadth_first()
        assert str(err.value) == "There is no node to traverse."
