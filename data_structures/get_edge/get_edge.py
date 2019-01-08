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

    def breadth_first(self, node=None):
        if node is None:
            print(f'There is no node to traverse.')
            raise TypeError(f'There is no node to traverse.')
        else:
            visited = {}
            for i in self.gdict.keys():
                visited[i] = 'Yay'

            queue = []
            queue.append(node)
            visited[node] = 'Nay'

            while queue:
                popped = queue.pop(0)
                print(popped)
                for what in self.gdict[popped]:
                    if visited[what] == 'Yay':
                        queue.append(what)
                        visited[what] = 'Nay'

    def flight_cost(self, node1=None, node2=None, node3=None):
        if node1 not in self.gdict.keys() or node2 not in self.gdict.keys():
            print('Invalid itinerary.')
        else:
            cost = 0
            if node2 not in self.gdict[node1]:
                print(False, '$', cost)
                return(False, '$', cost)
            else:
                cost += self.gdict[node1][node2]

                if node3 is not None and node3 not in self.gdict.keys():
                    print(False, '$', cost)
                    return(False, '$', cost)
                elif node3 in self.gdict.keys() and node3 not in self.gdict[node2]:
                    print(False, '$', cost)
                    return(False, '$', cost)
                elif node3 in self.gdict.keys() and node3 in self.gdict[node2]:
                    cost += self.gdict[node2][node3]
                
                print(True, '$', cost)


map = {
        'Pandora': {'Arendelle': 150, 'Metroville': 82},
        'Arendelle': {'Pandora': 150, 'Metroville': 99, 'New Monstropolis': 42},
        'Metroville': {'Pandora': 82, 'Arendelle': 99, 'New Monstropolis': 105, 'Naboo': 26, 'Narnia': 37},
        'New Monstropolis': {'Arendelle': 42, 'Metroville': 105, 'Naboo': 73},
        'Naboo': {'New Monstropolis': 73, 'Metroville': 26, 'Narnia': 250},
        'Narnia': {'Metroville': 37, 'Naboo': 250}
    }
g = Graph(map)



g.flight_cost('Arendelle', 'Pandora')
