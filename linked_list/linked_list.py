"""This module contains a class LinkedList which generate new nodes from an empty ll."""
from .node import Node
# from node import Node


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

    def insertBefore(self, value, newVal):
        """To insert newVal right before the matched value in the linked list."""
        current = self.head
        if current is None:
            self.head = Node(newVal)
            self._size += 1
            return

        if current.val == value:
            self.head = Node(newVal, self.head)
            self._size += 1
            return

        while current._next:
            if current._next.val == value:
                current._next = Node(newVal, current._next)
                self._size += 1
                return
            current = current._next
        else:
            print('There is no matched value in the linked list.')
        return


    def insertAfter(self, value, newVal):
        """To insert newVal right after the matched value in the linked list."""
        current = self.head
        if current is None:
            self.head = Node(newVal)
            self._size += 1
            return

        if current.val == value:
            self.head = Node(newVal, current)
            self._size += 1
            return

        while current._next:
            if current.val == value:
                print('found match!')
                current._next = Node(newVal, current._next)
                self._size += 1
                return
            current = current._next
        else:
            print('There is no matched value in the linked list.')
        return

# #FOR RUNNING PYTHON LINKED_LIST.PY IN THE TERMINAL:
# fix = LinkedList()
# fix.append('apple')
# fix.append('banana')
# fix.append('cucumber')
# fix.append('date')
# fix.append('elderberry')

# fix.insertAfter('cannotfind', 'after-date')


# #TO PRINT:
# result = fix.head
# while result:
#     print(result.val)
#     result = result._next



