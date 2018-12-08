"""This module contains class Node to create new nodes."""


class Node(object):
    """This class is set up to create new Nodes."""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f'{ self.value }'

    def __repr__(self):
        return f'<NODE: { self.value }>'
