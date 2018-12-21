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
        pass

    def __str__(self):
        pass

    def __len__(self):
        pass

    def add_vert(self, val):
        """
        """
        # add vertice to self.graph (i.e. self.gdict)
        if val in self.gdict:
            print('vert already exists.')
            return
        if val not in self.gdict:
            self.gdict[val] = {}
        # check to see if the vert already exists: if so raise exception

    def has_vert(self, val):
        """
        """
        if val in self.gdict:
            print(True)
            return(True)
        if val not in self.gdict:
            print(False)
            return(False)

    def add_edge(self, v1, v2, weight):
        """
        """
        if v1 not in self.gdict:
            print('There is no existing vert.')
            return
        # if v2 not in self.gdict[v1]:
        #     print('I am going to add an edge!')
        self.gdict[v1][v2] = weight
        print(self.gdict) 
        return self.gdict

    def get_neighbors(self, val):
        """
        """
        if val not in self.gdict:
            print('There is no existing vert.')
            return
        
        


graph_elements = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {'E': 1},
        'D': {'A': 5},
        'E': {'F': 2, 'B': 4},
        'F': {'D': 11}
    }

g = Graph(graph_elements)

g.add_edge('A', 'C', 0)
g.add_edge('A', 'C', 5)
g.add_edge('A', 'ABC', 100)

g.get_neighbors('efg')











