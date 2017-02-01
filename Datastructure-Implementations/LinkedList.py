"""LinkedList implementation"""
class Node:
    """Node class"""
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList:
    """Linked list class"""
    def __init__(self):
        self.head = None

    def add(self, item):
        """
        Add item to LinkedList
        args:
            param1: item to be added
        Usage: LinkedList.add(item)
        """
        self.head = Node(item, self.head)

    def remove(self):
        """
        Remove first item from LinkedList
        Usage: LinkedList.remove()
        """
        if self.is_empty():
            return None
        item = self.head.item
        self.head = self.head.next
        return item

    def is_empty(self):
        """
        Check if LinkedList is empty
        Usage: LinkedList.isempty()
        """
        return self.head is None

    def remove_last(self):
        """
        Remove last item from LinkedList
        Usage: LinkedList.remove()
        """
        ptr = self.head
        tmp = ptr
        while ptr.next != None:
            tmp = ptr
            ptr = ptr.next
        tmp.next = None

    def __str__(self):
        """Print list"""
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += ptr.item + " "
            ptr = ptr.next
        return tmp_str


