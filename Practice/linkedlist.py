class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None #for doubly linked list as it can traverse in both directions
class linked_list:
    def __init__(self) -> None:
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        last_node = self.head # start from the starting
        # here we use variable last_node sincewe are each time changing value of last_node to last_node.next
        # so it will be difficult to keep track of self.head
        while last_node != None:
            last_node = last_node.next
        last_node.next = new_node   
    def insert(self, pos, data):
        new_node = Node(data)
        current = self.head
        for i in range(pos-1):
            current = current.next
        #current node goes to pos-1 so current.next is the position for the new node and current.next is
        #now shifted to new_node.next and new_node is assigned current.next
        new_node.next = current.next 
        current.next = new_node
    def remove(self, item):
        current = self.head
        prev = None  #pointer to keep track of previous node
        while current and current.data != item:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next # here current is already pointing to current.next
        current = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
    def add(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node