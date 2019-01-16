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


class BST(object):
    """To create a node(s) for a binary search tree and its related methods."""

    def __init__(self, iterable=None):
        self.root = None
        self._size = 0
        self.set_one = set()

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

    def post_order_set(self, node=None):
        if self.root is None:
            raise TypeError(f'There is no node to traverse.')
        else:
            if node.left:
                self.post_order_set(node.left)
            if node.right:
                self.post_order_set(node.right)
            self.set_one.add(node.val)
            print(node.val)
            print(self.set_one)
    
    def tree_intersection(self, tree_two):
        self.set_one = set()
        self.post_order_set(tree_two.root)
        return


tree_one = BST([10, 12, 11, 15, 20, 17])
tree_two = BST([40, 15, 47, 20, 30, 50, 65])

# tree_one.tree_intersection(tree_two)
tree_one.tree_intersection(tree_two)

# IN-ORDER BASED ON [10, 12, 11, 15, 20, 17]: 10, 11, 12, 15, 17, 20
# PRE-ORDER BASED ON [10, 12, 11, 15, 20, 17]: 10, 12, 11, 15, 20, 17
