"""This module contains class AnimalShelter that works like a queue."""


class Node(object):
    """This class is set up to create new Nodes."""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f'{ self.value }'

    def __repr__(self):
        return f'<NODE: { self.value }>'


class AnimalShelter(object):
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
        if self.front is None:
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

    def dequeue(self, val):
        """
        """
        if self.front is None:
            raise TypeError(f'Input must be a non-empty queue.')
        else:
            current = Node(None, self.front)
            loop = 0
            while current.next_node:
                if current.next_node.value == val:
                    if loop == 0:
                        self.front = self.front.next_node
                        current.next_node.next_node = None
                        return current.next_node
                    else:
                        if self.rear == current.next_node:
                            self.rear = current
                        temp = current.next_node
                        current.next_node = current.next_node.next_node
                        # print('deleted node value is: ', temp.value)
                        return temp
                else:
                    loop = loop + 1
                    current = current.next_node



############################################
####          TO PRINT:                 ####
####                                    ####
############################################

# test_queue = AnimalShelter([1, 2, 3, 4, 5])
# test_queue.enqueue(6)
# test_queue.enqueue(7)
# test_queue.dequeue(7)

# current = test_queue.front
# while current:
#     print(current.value)
#     current = current.next_node


# print('front: ', test_queue.front.value)
# print('rear: ', test_queue.rear.value)
