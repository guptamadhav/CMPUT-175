class Node:
    def __init__(self, data) -> None:
        self.data = data
        self. next = None
        self.prev = None
class SLinkedList:
    def __init__(self):
        self.head = None
    def add(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            #assign the current head to next node of new node and assign new node to the head
            new_node.next = self.head
            self.head = new_node
    def append(self, item):
        if self.head == None:
            self.add(item)
            return
        new_node = Node(item)
        current = self.head
        while current != None:
            current = current.next
        # here current does not refernce to any node and thus means it is the next reference to last node and 
        # thus new node is assigned to it
        current = new_node
    def remove(self, item):
        if self.head.data == item:
            self.head = self.head.next
            return
        