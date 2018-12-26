"""This module will contain class Graph and its related methods."""


class Graph:
    """
    """
    def __init__(self, iterable=None):
        if iterable is None:
            iterable = {}

        if type(iterable) is not dict:
            raise TypeError('Iterable is not a dictionary.')

        # "gdict" will be the "graph" in conftest
        self.gdict = iterable
        # self.graph = iterable

    def __repr__(self):
        output = f'<List of vertices: { self.gdict.keys() }>'
        # <List of vertices: dict_keys(['G', 'B', 'C', 'D', 'E', 'F'])>
        return output

    def __str__(self):
        output = f'The list of vertices are: {self.gdict.keys()}'
        # "The list of vertices are: dict_keys(['G', 'B', 'C', 'D', 'E', 'F'])"
        return output

    def __len__(self):
        return len(self.gdict.keys())

    def add_vert(self, val):
        """
        """
        # add vertice to self.graph (i.e. self.gdict)
        if type(val) is not float and type(val) is not str:
            print('Val must be a string or a number.')
            raise KeyError('Val must be a string or a number.')
        if val in self.gdict:
            print('Vert already exists.')
            raise KeyError('Vert already exists.')

        self.gdict[val] = {}

    def has_vert(self, val):
        """
        """
        if val in self.gdict:
            print(True)
            return(True)
        print(False)
        return(False)

    def add_edge(self, v1, v2, weight):
        """
        """
        if v1 not in self.gdict:
            print('The vert does not exist.')
            raise KeyError('The vert does not exist.')
        self.gdict[v1][v2] = weight
        print(self.gdict) 
        return self.gdict

    def get_neighbors(self, val):
        """
        """
        if val not in self.gdict:
            print('There is no existing vert.')
            raise KeyError('There is no existing vert.')
        print(self.gdict[val].keys())
        return self.gdict[val].keys()


# graph_elements = {
#         'A': {'B': 10, 'C': 15},
#         'B': {'D': 15, 'E': 5, 'C': 2},
#         'C': {'F': 50, 'G': 25},
#         'D': {},
#         'E': {'C': 5},
#         'F': {'E': 10},
#         'G': {'F': 20}
#     }
# g = Graph(graph_elements)

# print(g.gdict)
