"""This module will contain fixtures to test graph.py."""

import pytest
from ..depth_first import Graph


@pytest.fixture()
def graph_empty():
    g = Graph()
    return g


@pytest.fixture()
def graph_one():
    g = Graph()
    g.gdict = {
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
    g.gdict = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g


@pytest.fixture()
def graph_map():
    map = {
            'Pandora': {'Arendelle': 150, 'Metroville': 82},
            'Arendelle': {'Pandora': 150, 'Metroville': 99, 'New Monstropolis': 42},
            'Metroville': {'Pandora': 82, 'Arendelle': 99, 'New Monstropolis': 105, 'Naboo': 26, 'Narnia': 37},
            'New Monstropolis': {'Arendelle': 42, 'Metroville': 105, 'Naboo': 73},
            'Naboo': {'New Monstropolis': 73, 'Metroville': 26, 'Narnia': 250},
            'Narnia': {'Metroville': 37, 'Naboo': 250}
        }
    g = Graph(map)
    return g

@pytest.fixture()
def graph_three():
    dictionary = {
        'A': {'B': 0, 'D': 0},
        'B': {'A': 0, 'C': 0, 'D': 0},
        'C': {'B': 0, 'G': 0},
        'D': {'A': 0, 'B': 0, 'E': 0, 'H': 0, 'F': 0},
        'E': {'D': 0},
        'F': {'D': 0, 'H': 0},
        'G': {'C': 0},
        'H': {'F': 0, 'D': 0},
        }
    g = Graph(dictionary)
    return g
    