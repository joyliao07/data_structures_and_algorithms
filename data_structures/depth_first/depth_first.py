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
        # This is a boolean itself:
        return val in self.gdict

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
            raise KeyError(False, '$0')
        else:
            cost = 0
            if node2 not in self.gdict[node1]:
                print(False, '$', cost)
                raise KeyError(False, '$', cost)
            else:
                cost += self.gdict[node1][node2]

                if node3 is not None and node3 not in self.gdict.keys():
                    print(False, '$', cost)
                    raise KeyError(False, '$', cost)
                elif node3 in self.gdict.keys() and node3 not in self.gdict[node2]:
                    print(False, '$', cost)
                    raise KeyError(False, '$', cost)
                elif node3 in self.gdict.keys() and node3 in self.gdict[node2]:
                    cost += self.gdict[node2][node3]
                
                print(True, '$', cost)
                return(True, '$', cost)

    # def depth_recursive(self, node, visited, stack):
    #     if visited[node] == 'New':
    #         print(node)
    #         stack.append(node)
    #         visited.append(node)
    #     for what in self.gdict[node]:
    #         if what not in visited:
    #             stack.append(what)
    #             print('stack is: ', stack)
    #             print('back to recursion')
    #             self.depth_recursive(what, visited, stack)

    def depth_first_traversal(self, node):

        visited = []
        stack = []

        if node not in self.gdict.keys():
            print('Node does not exist.')
            raise KeyError('Node does not exist.')
        else:
            if node not in visited:
                print(node)
                stack.append(node)
                visited.append(node)










map = {
        'A': {'B':0, 'D':0},
        'B': {'A':0, 'D':0, 'C':0},
        'C': {'B':0, 'G':0},
        'D': {'A':0, 'B':0, 'E':0, 'F':0, 'H':0},
        'E': {'D':0},
        'F': {'D':0, 'H':0},
        'G': {'C':0},
        'H': {'F':0, 'D':0},
    }
g = Graph(map)

g.depth_first_traversal('A')
