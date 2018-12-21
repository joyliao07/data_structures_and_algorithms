"""This module will contain fixtures to test graph.py."""

import pytest
from .graph import Graph


@pytest.fixture()
def graph_empty():
    g = Graph()
    return g


@pytest.fixture()
def graph_one():
    g = Graph()
    g.graph = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {'E': 1},
        'D': {'A': 5},
        'E': {'F': 2, 'B': 4},
        'F': {'D': 11}
    }
    return g


@pytest.fixture()
def graph_two():
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g
