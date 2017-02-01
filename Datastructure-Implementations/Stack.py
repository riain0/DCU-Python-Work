"""
Implementation of a stack.
"""
class Stack:
    """
    Python implementation of a stack.
    """
    def __init__(self, capacity=10):
        self.data = [0] * capacity
        self.top = 0

    def isempty(self):
        """
        Checks if the stack is empty.
        """
        return self.top == 0

    def push(self, item):
        """
        Pushes param2 onto the Stack

        Args:
            self: gets class variables
            item: item to push onto the stack
        """
        if self.top < len(self.data):
            self.data[self.top] = item
        else:
            raise Exception("The Stack is full!")
        self.top += 1

    def pop(self):
        """
        Removes last item from the stack
        """
        if self.isempty():
            return None
        else:
            self.top -= 1
            return self.data[self.top]
