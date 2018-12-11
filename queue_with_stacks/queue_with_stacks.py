"""Using two methods from Stack, accomplish enqueue and dequeue."""
# from .. stack.stack import Stack
# from .. stack.stack import Node
class Node(object):
    """This class is set up to create new Nodes."""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f'{ self.value }'

    def __repr__(self):
        return f'<NODE: { self.value }>'

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


################################################
#####               NEW CLASS:             #####   
#####                                      #####   
################################################
class PseudoQueue(object):

    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value):
        self.stack_1.push(value)
        self.rear = self.stack_1.top

    def dequeue(self):
        while self.stack_1.top:
            self.stack_2.push(self.stack_1.pop().value)

        popped = self.stack_2.pop()

        while self.stack_2.top:
            self.stack_1.push(self.stack_2.pop().value)

        self.rear = self.stack_1.top
        return popped


#####               TO PRINT :             #####   
################################################

new_pseudoqueue = PseudoQueue()

new_pseudoqueue.enqueue('apple')
new_pseudoqueue.enqueue('banana')
new_pseudoqueue.enqueue('cucumber')
new_pseudoqueue.dequeue()
new_pseudoqueue.dequeue()

print(new_pseudoqueue.stack_1.top.value)
print(len(new_pseudoqueue.stack_1))
