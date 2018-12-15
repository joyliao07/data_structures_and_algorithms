"""This module contains class BST and its related methods."""


class Node(object):
    """This class is set up to create new Nodes."""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{ self.val }'

    def __repr__(self):
        return f'<NODE: { self.val }>'


class BST(object):
    """To create a node(s) for a binary search tree and its related methods."""

    def __init__(self, iterable=None):
        # self.front = None
        self.root = None
        self._size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('Iterable is not a list.')

        for what in iterable:
            self.add(what)

    def __str__(self):
        output = f'Value of the root Queue is: {self.root.val}'
        return output

    def __len__(self):
        return self._size

    def __repr__(self):
        return f'<BST root: { self.root.val }>'

    def add(self, val):
        """
        """
        if self.root is None:
            new_node = Node(val)
            self.root = new_node
            print('self.root is added: ', self.root.val)
            self._size += 1
            return self
        
        else:
            new_node = Node(val)
            self._size += 1

            current = self.root
            print('add new_node below root level: ', new_node.val)

            while current:
                print('inside while loop, new_node.val is: ', new_node.val)
                if current.val == val:
                    return
                if current.val > val:
                    print('current will be move to the left: ', new_node.val)
                    current = current.left
                else:
                    print('current will be move to the right: ', new_node.val)
                    current = current.right

            current = new_node
            print('current.val is: ', current.val)
            print('self.root.right.val is: ', self.root.right.val)



            # if current.val == val:
            #     return
            # elif current.val > val:
            #     current.left = new_node
            #     print('new_node is added to the left: ', current.left.val)
            # else:
            #     current.right = new_node
            #     print('new_node is added to the right: ', current.right.val)


new_tree = BST([10, 12])

# 10
print(new_tree.root.val)
# 12
print(new_tree.root.right.val)
# print(new_tree.root.right.left.val)



















