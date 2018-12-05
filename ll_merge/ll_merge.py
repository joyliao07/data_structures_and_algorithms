"""Code Challenge 08"""
# from ..linked_list.linked_list import LinkedList
# from ..linked_list.node import Node


class Node(object):
    """
    """
    def __init__(self, val, _next=None):
        self.val = val
        self._next = _next

    def __str__(self):
        output = f'{ self.val }'
        return output


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
        """To insert a value to the linked list."""
        self.head = Node(value, self.head)
        self._size += 1

    def includes(self, searched):
        """ To tell whether the ll includes the designated valude."""
        current = self.head

        while current:
            if current.val == searched:
                return True
            current = current._next
        return False

    def append(self, newVal):
        """To insert newVal to the tail of the linked list."""
        current = self.head
        if current is None:
            self.head = Node(newVal)
            self._size += 1
            return

        while current._next:
            current = current._next

        current._next = Node(newVal)
        self._size += 1







test = LinkedList([3, 2, 3])

print(test.head.val)




















