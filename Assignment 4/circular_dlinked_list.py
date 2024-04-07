#i didnt use Lab 7 code for linked list because i wanted to learn and practice references on my own and
#i had to code it on my own to debug it to understand better
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.current = None # to keep the reference of current node
    def circular(self):
        if self.head is not None:
            self.tail.next = self.head
            self.head.prev = self.tail
    def add(self, item):
        # to begin the linked list
        new_node = Node(item)
        self.head = new_node
        self.tail = new_node
        self.current = self.head
    def addLeft(self, item):
        new_node = Node(item)
        if self.current == self.head:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.prev = self.current.prev
            new_node.next = self.current
            self.current.prev.next = new_node
            self.current.prev = new_node
        self.current = new_node
        self.circular()
    def addRight(self,item):
        new_node = Node(item)
        if self.current == self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            new_node.next = self.current.next
            new_node.prev = self.current
            self.current.next.prev = new_node
            self.current.next = new_node
        self.current = new_node
        self.circular()
    def deleteCurrent(self):
        previous = self.current.prev
        next_n = self.current.next
        previous.next = self.current.next
        next_n.prev = self.current.prev
        del self.current
        if previous and self.head:
            self.current = previous
        elif next_n and self.tail:
            self.current = next_n
    def getRight(self):
        tmp = self.current.next
        self.current = tmp

    def getLeft(self):
        tmp = self.current.prev
        self.current = tmp

    def getData(self):
        return self.current.data
    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head

        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()
