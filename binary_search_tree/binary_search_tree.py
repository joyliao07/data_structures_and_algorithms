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

    def prep(self, val):
        pass

    def add_node(self, val):
        """
        """
        print('line 50 start to create new node: ', val)
        if self.root is None:
            self.root = Node(val)
            print('root is created outside insersion: ', self.root.val)
            return

        def insersion(node, val):
            print('line 57 start to insert val: ', val)
            if node is None:
                node = Node(val)
                print('line 60 root is created: ', node.val)
                return
            if node.val < val:
                print('line 63 node.val is: ', node.val)
                if node.right is None:
                    node.right = Node(val)
                    print('line 66 created node.right: ', node.right.val)
                    return
                else:
                    print('line 68 to call insersion and pass in node.right: ', node.right.val)
                    print('line 69 to call insersion and pass in val: ', val)
                    insersion(node.right, val)
                    return
            elif node.val > val:
                print('line 72 node.val is: ', node.val)
                if node.left is None:
                    node.left = Node(val)
                    print('line 75 created node.left: ', node.left.val)
                    return
                else:
                    print('line 77 to call insersion and pass in node.left: ', node.left.val)
                    print('line 78 to call insersion and pass in val: ', val)
                    insersion(node.left, val)
                    return

        insersion(self.root, val)



new_tree = BST([10, 12, 11, 15, 20, 17])

# 10
print(new_tree.root.val)
# 12
print(new_tree.root.right.val)
# 11
print(new_tree.root.right.left.val)
# 15
print(new_tree.root.right.right.val)
# 20
print(new_tree.root.right.right.right.val)
# 17
print(new_tree.root.right.right.right.left.val)



















