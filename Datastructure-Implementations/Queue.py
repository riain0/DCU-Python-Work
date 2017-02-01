"""Queue implementation"""
class Queue:
    """Queue class"""
    def __init__(self, capacity=10):
        self.data = [0] * capacity
        self.front = 0
        self.back = 0

    def count(self):
        """
        Count elements in Queue
        Usage: Queue.count()
        """
        if self.back >= self.front:
            return self.back - self.front
        else:
            return self.back - self.front + len(self.data)

    def isempty(self):
        """
        Checks if Queue is empty
        Usage: Queue.isempty()
        """
        return self.front == self.back

    def enqueue(self, item):
        """
        Push an item onto the Queue
        args:
            param1: item to be pushed onto the Queue
        Usage: Queue.enqueue(item)
        """
        if self.count() < len(self.data) - 1:
            self.data[self.back] = item
            self.back = (self.back + 1) % len(self.data)
        else:
            print("Queue Full")

    def dequeue(self):
        """
        Removes item from Queue using FIFO algorithm
        Usage:
            Queue.dequeue()
        """
        if self.count() > 0:
            item = self.data[self.front]
            self.front = (self.front + 1) % len(self.data)
            return item
        else:
            return None
