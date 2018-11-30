"""This module contains a class LinkedList which generate new nodes from an empty ll."""
# from node import Node
from .node import Node


class LinkedList(object):
    """To generate linked lists with input values."""

    def __init__(self, iterable=None):
        self.head = None
        self._size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('Iterable must be of type list.')

        for val in iterable:
            self.insert(val)

    def __str__(self):
        output = f'Linked List: Head val is: {self.head}'
        return output

    def __repr__(self):
        output = f'<LinkedList: head - {self.head} size - {self._size} >'
        return output

    def __len__(self):
        return self._size

    def insert(self, value):
        """
        """
        # node = Node(value)... 
        self.head = Node(value, self.head)
        self._size += 1

    def includes(self, searched):
        """ To tell whether the ll includes the designated valude.
        """
        p = self.head.val
        if p is None:
            return False
        while p is not None:
            if p == searched:
                return True
            p = p._next
        return False


print(LinkedList([1, 2, 3]))




