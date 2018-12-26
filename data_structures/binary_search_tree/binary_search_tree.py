"""This module contains class BST and its related methods."""


class NodeTree(object):
    """This class is set up to create new Nodes."""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{ self.val }'

    def __repr__(self):
        return f'<NODE: { self.val }>'


class NodeQueue(object):
    """This class is set up to create new Nodes."""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f'{ self.value }'

    def __repr__(self):
        return f'<NODE: { self.value }>'


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

    def __repr__(self):
        return f'<Queue front: { self.front.value }>'

    def enqueue(self, value):
        """
        """
        if self.front is None:
            new_node = NodeQueue(value)
            self.front = new_node
            self.rear = new_node
            self._size += 1
            return self
        else:
            new_node = NodeQueue(value)
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


class BST(object):
    """To create a node(s) for a binary search tree and its related methods."""

    def __init__(self, iterable=None):
        self.root = None
        self._size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('Iterable is not a list.')

        for what in iterable:
            self.add_node(what)

    def __str__(self):
        output = f'Value of the root Queue is: {self.root.val}'
        return output

    def __len__(self):
        return self._size

    def __repr__(self):
        return f'<BST root: { self.root.val }>'

    def add_node(self, val):
        """
        """
        # print('line 50 start to create new node: ', val)
        if self.root is None:
            self.root = NodeTree(val)
            # print('root is created outside insersion: ', self.root.val)
            return

        def insersion(node, val):
            # print('line 57 start to insert val: ', val)
            if node is None:
                node = NodeTree(val)
                # print('line 60 root is created: ', node.val)
                return
            if node.val < val:
                # print('line 63 node.val is: ', node.val)
                if node.right is None:
                    node.right = NodeTree(val)
                    # print('line 66 created node.right: ', node.right.val)
                    return
                else:
                    # print('line 68 to call insersion and pass in node.right: ', node.right.val)
                    # print('line 69 to call insersion and pass in val: ', val)
                    insersion(node.right, val)
                    return
            elif node.val > val:
                # print('line 72 node.val is: ', node.val)
                if node.left is None:
                    node.left = NodeTree(val)
                    # print('line 75 created node.left: ', node.left.val)
                    return
                else:
                    # print('line 77 to call insersion and pass in node.left: ', node.left.val)
                    # print('line 78 to call insersion and pass in val: ', val)
                    insersion(node.left, val)
                    return

        insersion(self.root, val)

    def in_order_traversal(self, node=None):
        if self.root is None:
            raise TypeError(f'There is no node to traverse.')
        else:
            if node.left:
                self.in_order_traversal(node.left)
            print(node.val)
            if node.right:
                self.in_order_traversal(node.right)

    def pre_order_traversal(self, node=None):
        if self.root is None:
            raise TypeError(f'There is no node to traverse.')
        else:
            print(node.val)
            if node.left:
                self.pre_order_traversal(node.left)
            if node.right:
                self.pre_order_traversal(node.right)
        
    def post_order_traversal(self, node=None):
        if self.root is None:
            raise TypeError(f'There is no node to traverse.')
        else:
            if node.left:
                self.post_order_traversal(node.left)
            if node.right:
                self.post_order_traversal(node.right)
            print(node.val)

    def breadth_first(self, root=None):
        if root is None:
            raise TypeError(f'There is no node to traverse.')
        else:
            que = Queue()
            #PASS IN THE ENTIRE NODE INSTEAD OF VAL INTO ENQUEUE()
            que.enqueue(root)

            while que.front is not None:
                front = que.dequeue()

                print(front.value.val)
                if front.value.left is not None:
                    que.enqueue(front.value.left)
                if front.value.right is not None:
                    que.enqueue(front.value.right)
    
    def find_maximum_value(self, root=None):
        if root is None:
            raise TypeError(f'There is no node to traverse.')
        else:
            que = Queue()
            que.enqueue(root)
            max_val = root.val

            while que.front is not None:
                front = que.dequeue()

                if max_val < front.value.val:
                    max_val = front.value.val

                if front.value.left is not None:
                    que.enqueue(front.value.left)
                if front.value.right is not None:
                    que.enqueue(front.value.right)
            
            print(max_val)
            return(max_val)



# new_tree = BST([10, 12, 11, 15, 20, 17])
two_tree = BST([40, 15, 47, 20, 30, 50, 65])

two_tree.find_maximum_value(two_tree.root)


# IN-ORDER BASED ON [10, 12, 11, 15, 20, 17]: 10, 11, 12, 15, 17, 20
# PRE-ORDER BASED ON [10, 12, 11, 15, 20, 17]: 10, 12, 11, 15, 20, 17

