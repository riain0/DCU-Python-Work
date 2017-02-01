"""
 BST: Binary Search Tree
"""
class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root is None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ...
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)

    # Use count to test.
    def rcount(self, ptr):
        """Recursively count leaves"""
        if ptr is None:
            return 0
        else:
            return 1 + self.rcount(ptr.left) + self.rcount(ptr.right)

    def count(self):
        """Use rcount"""
        return self.rcount(self.root)

    def rheight(self, ptr):
        """Recursively get the height of the tree"""
        if ptr is None:
            return 0
        else:
            return 1 + max(self.rheight(ptr.left), self.rheight(ptr.right))

    def in_order(self, ptr):
        """Check if the tree is in-order"""
        if ptr is None:
            return ""
        else:
            return self.in_order(ptr.left) + str(ptr.item) + "," + self.in_order(ptr.right)

    def __str__(self):
        return self.in_order(self.root)

    def height(self):
        """Use rheight"""
        return self.rheight(self.root)

    def odd_recursive_count(self, ptr):
        """Recursively count odd elements of BST"""
        if self is None:  # Base Case
            return 0
        else:
            if ptr.item % 2:
                return self.odd_recursive_count(ptr.left) + self.odd_recursive_count(ptr.right) + 1
            return self.odd_recursive_count(ptr.left) + self.odd_recursive_count(ptr.right)

    def or_count(self):
        """Use odd_recursive_count"""
        return self.odd_recursive_count(self.root)
