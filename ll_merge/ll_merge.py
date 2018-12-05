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


ll_A = LinkedList([1, 2, 3])
ll_B = LinkedList(['A', 'B', 'C'])


def ll_merge(ll_A, ll_B):
    """
    """
    A = ll_A.head
    B = ll_B.head
    new = LinkedList()
    new.head = Node('haha')

    # #THIS WORKING:
    # new.head = Node('haha')
    # new.head._next = Node(A.val)

    current = new.head
    while A or B:
        if A:
            current._next = Node(A.val)
            print('current in A is: ', current._next.val)
            current = current._next
            # print('test2: ', current._next.val)
            A = A._next
            if B:
                current._next = Node(B.val)
                print('current in B is: ', B)
                current = current._next
                B = B._next

                P = new.head
                while P:
                    print(P.val)
                    P = P._next

        # if B:
        #     current._next = None
        # return


    print('start to print:')

    current = new.head
    while current:
        print(current.val)
        current = current._next

    return




ll_merge(ll_A, ll_B)


















