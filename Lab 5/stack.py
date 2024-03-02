#----------------------------------------------------
# Stack implementation #2 
# (Top of stack corresponds to back of list)
# 
# Author: CMPUT 175 team
# Updated by:
#----------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
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
        pass       
s = Stack()
s.push(1)
s.push(2)
s.push(3)
if s.pop() == 3:
    s.push("a")
if s.peek() == "a":
    s.pop()
print(s.pop())