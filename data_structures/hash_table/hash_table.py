"""This module will contain class Hash and its related methods."""


class Hash(object):
    """
    """
    def __init__(self, iterable=None):
        # if iterable is None:
        #     iterable = {}

        # if type(iterable) is not dict:
        #     raise TypeError('Iterable is not a dictionary.')

        # self.gdict = iterable
        # self.graph = iterable

    def __repr__(self):
        # output = f'<List of vertices: { self.gdict.keys() }>'
        output = f'<repr string...>'
        return output

    def __str__(self):
        # output = f'The list of vertices are: {self.gdict.keys()}'
        output = f'Str...'
        return output

    def __len__(self):
        # return len(self.gdict.keys())
        return

    def create_hash(self, val):
        """
        """
        # What is the format of input?
        # if type(val) is not float and type(val) is not str:
        #     print('Val must be a string or a number.')
        #     raise KeyError('Val must be a string or a number.')
        # if val in self.gdict:
        #     print('Vert already exists.')
        #     raise KeyError('Vert already exists.')

        # self.gdict[val] = {}

    # def has_vert(self, val):
    #     """
    #     """
    #     # This is a boolean itself:
    #     return val in self.gdict

    # def add_edge(self, v1, v2, weight):
    #     """
    #     """
    #     if v1 not in self.gdict:
    #         print('The vert does not exist.')
    #         raise KeyError('The vert does not exist.')
    #     self.gdict[v1][v2] = weight
    #     print(self.gdict) 
    #     return self.gdict

    # def get_neighbors(self, val):
    #     """
    #     """
    #     if val not in self.gdict:
    #         print('There is no existing vert.')
    #         raise KeyError('There is no existing vert.')
    #     print(self.gdict[val].keys())
    #     return self.gdict[val].keys()




map = {
        'A': {'B':0, 'D':0},
        'B': {'A':0, 'C':0, 'D':0},
        'C': {'B':0, 'G':0},
        'D': {'A':0, 'B':0, 'E':0, 'H':0, 'F':0},
        'E': {'D':0},
        'F': {'D':0, 'H':0},
        'G': {'C':0},
        'H': {'F':0, 'D':0},
    }
g = Graph(map)

g.depth_first_traversal('A')
