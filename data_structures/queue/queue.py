"""This module contains class Queue for Queue-related methods."""
from .node import Node
# from node import Node


class Queue(object):
    """To create a node for a Queue and other related methods."""

    def __init__(self, iterable=None):
        self.front = None
        self.rear = None
        self._size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('Iterable is not a list.')

        for what in iterable:
            self.enqueue(what)

    def __str__(self):
        output = f'Queue: Value of the front Queue is: {self.front.value}'
        return output

    def __len__(self):
        return self._size

    def __repr__(self):
        return f'<Queue front: { self.front.value }>'

    def enqueue(self, value):
        """
        """
        if self.front is None and self.rear is None:
            new_node = Node(value)
            self.front = new_node
            self.rear = new_node
            self._size += 1
            return self
        else:
            new_node = Node(value)
            self.rear.next_node = new_node
            self.rear = new_node
            self._size += 1
            return self

    def dequeue(self):
        """
        """
        if self.front is None or self.rear is None:
            return f'Input must be a non-empty queue.'
        else:
            temp = self.front
            self.front = self.front.next_node
            temp.next_node = None
            return temp

    def peek(self):
        """
        """
        try:
            return self.front.value
        except:
            return f'Input must be a non-empty queue.'


################################################
#####               To print:              #####   
#####                                      #####   
################################################

new_queue = Queue([1, 2, 3, 4, 5, 6])

new_queue.enqueue(7)
new_queue.dequeue()
new_queue.dequeue()


print(new_queue.rear.value)
