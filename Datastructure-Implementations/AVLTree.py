"""
A python implementation of an AVL Tree
"""
from Node import Node

class AVLTree:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    def add(self, item):
        """ Add this item to its correct position on the tree """
        if self.root is None:
            self.root = Node(item, None, None)
        else:
            parent_stack = [] # Use a list as a stack to hold parents
            child_tree = self.root
            while child_tree != None:
                parent_stack.append(child_tree)
                if item < child_tree.item:
                    child_tree = child_tree.left
                else:
                    child_tree = child_tree.right

            # child_tree is pointing to the new node, but we've gone too far
            # we need to get to the parent to change its pointer
            parent = parent_stack[-1]       # The parent is the last item on the parent stack
            node = Node(item, None, None)
            if item < parent.item: # left?
                parent.left = node
            elif item > parent.item: # right?
                parent.right = node
            else:
                # Else this item is already in the tree and so not added
                return

            # The item has been added, now see if we are AVL unbalanced - go back up the tree.
            while node != None:
                if abs(self.recurse_height(node.left) - self.recurse_height(node.right)) > 1:
                    # Found an out of order node! Need to fix
                    # First get the three nodes to restructure
                    top = node
                    mid = top.left if item < top.item else top.right
                    bot = mid.left if item < mid.item else mid.right

                    # Work out which rotation we need to do. (which one is in the middle)
                    if top.item < mid.item < bot.item:
                        # mid in the middle => put on top
                        new_top = mid
                        top.right = mid.left
                        mid.left = top
                    elif bot.item < mid.item < top.item:
                        # Right rotation
                        new_top = mid
                        top.left = mid.right
                        mid.right = top
                    elif mid.item < bot.item < top.item:
                        # double 1
                        new_top = bot
                        mid.right = bot.left
                        top.left = bot.right
                        bot.left = mid
                        bot.right = top
                    else:# top.item < bot.item < mid.item:
                        # double 2
                        new_top = bot
                        mid.left = bot.right
                        top.right = bot.left
                        bot.left = top
                        bot.right = mid

                    # Make the parent of top point to the new top
                    top_parent = None if len(parent_stack) == 0 else parent_stack.pop()
                    if top_parent is None:
                        self.root = new_top
                    elif top.item < top_parent.item:
                        top_parent.left = new_top
                    else:
                        top_parent.right = new_top
                    break

                node = None if len(parent_stack) == 0 else parent_stack.pop()

    def recursive_contains(self, item, ptr):
        """ returns a pointer to the node rather than a boolean, None if not present """
        if ptr is  None:
            return None
        else:
            if item == ptr.item:
                return ptr
            elif item < ptr.item:
                return self.recursive_contains(item, ptr.left)
            else:
                return self.recursive_contains(item, ptr.right)

    def contains(self, item):
        """ returns a pointer to the node rather than a boolean, None if not present """
        return self.recursive_contains(item, self.root)

    def recurse_height(self, ptr):
        """Recursively find the height of the tree"""
        if ptr is None:
            return 0
        else:
            return 1 + max(self.recurse_height(ptr.left), self.recurse_height(ptr.right))

    def height(self):
        """Use recursive height function"""
        return self.recurse_height(self.root)

    def recurse_str(self, ptr):
        """Allow printing"""
        if ptr is None:
            return ""
        else:
            return self.recurse_str(ptr.left) + str(ptr.item) + "," + self.recurse_str(ptr.right)

    def __str__(self):
        return self.recurse_str(self.root)
