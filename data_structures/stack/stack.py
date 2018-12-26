"""This module contains class Stack for stack-related methods."""
from .node import Node
# from node import Node


class Stack(object):
    """To create a node for a stack and other related methods."""

    def __init__(self, iterable=None):
        self.top = None
        self._size = 0

        if iterable is None:
            iterable = []
        
        if type(iterable) is not list:
            raise TypeError('Iterable is not a list.')

        for what in iterable:
            self.push(what)

    def __str__(self):
        output = f'Stack: Value of the top stack is: {self.top.value}'
        return output

    def __len__(self):
        return self._size

    def __repr__(self):
        return f'<STACK Top: { self.top }>'

    def push(self, value):
        """
        """
        self.top = Node(value, self.top)
        # node = Node(value)
        # node.next_node = self.top
        # self.top = node
        self._size += 1
        return self

    def pop(self):
        """
        """
        if self.top:
            old_top = self.top
            self.top = old_top.next_node
            old_top.next_node = None
            self._size -= 1
            return old_top
        else:
            return f'Input stack cannot be empty.'

    def peek(self):
        """
        """
        try:
            return self.top.value
        except:
            return f'Input must be a non-empty stack.'


################################################
#####               To print:              #####   
#####                                      #####   
################################################

new_stack = Stack([1, 2, 3, 4])

# new_stack.push(5)
# new_stack.pop()
# new_stack.pop()
# new_stack.pop()

print(type(new_stack))
