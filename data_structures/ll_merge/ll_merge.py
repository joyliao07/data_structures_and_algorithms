"""Code Challenge 08 ll_merge."""
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

#####################################
###         ll_merge():           ###
###                               ###
#####################################


def ll_merge(ll_A, ll_B):
    """The function will take in two linked list, zip them, and return the result as one linked list.
    """
    A = ll_A.head
    B = ll_B.head
    # new = LinkedList()

    current = None
    while A or B:
        if A:
            if current is None:
                current = Node(A.val)
                new_head = current
                A = A._next
            else:
                current._next = Node(A.val)
                current = current._next
                A = A._next

            # new.append(A.val)
            # A = A._next

        if B:
            current._next = Node(B.val)
            current = current._next
            B = B._next

            # new.append(B.val)
            # B = B._next

    return new_head

#####################################
###   Call function to print:     ###
###                               ###
#####################################

ll_A = LinkedList([1, 2])
ll_B = LinkedList(['A', 'B', 'C'])

# ll_merge(ll_A, ll_B)
print(ll_merge(ll_A, ll_B))
print(ll_merge(ll_A, ll_B)._next)
print(ll_merge(ll_A, ll_B)._next._next)
print(ll_merge(ll_A, ll_B)._next._next._next)
print(ll_merge(ll_A, ll_B)._next._next._next._next)


# See https://codereview.stackexchange.com/questions/113670/merge-two-linked-lists-in-python














