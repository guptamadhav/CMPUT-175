class Stack:
    def __init__(self):
        self.items = []
        self.__capacity = 4

    def push(self, item):
        if len(self.items)<=self.__capacity:
            self.items.append(item)
        else:
            raise Exception("pushError")
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def pop(self):  
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("Can not pop from an empty stack")
    
    # MODIFY: RAISE AN EXCEPTION IF THIS METHOD IS INVOKED ON AN EMPTY STACK
    def peek(self):  
        if not self.isEmpty():
            return self.items[len(self.items)-1] 
        else:
            raise IndexError("Can not pop from an empty stack")

    def isEmpty(self):
        return self.items == []
    
    def isFull(self):
        return len(self.items) == self.__capacity
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        #TO DO: complete method according to updated ADT
        while not self.isEmpty():
            self.items.pop()
