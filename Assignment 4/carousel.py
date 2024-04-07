from circular_dlinked_list import CircularDoublyLinkedList
import json
import os
import art
import time
def clear_screen():
    '''
    Clears the terminal screen for future contents.
    Input: N/A
    Returns: N/A
    '''
    if os.name == "nt":  # windows
        os.system("cls")
    else:
        os.system("clear")  # unix (mac, linux, etc.)
def print_location(x, y, text): #from lab 5
    '''
    Prints text at the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
        - text (str): text to print
    Returns: N/A
    '''
    print ("\033[{};{}H{}".format(x, y, text))

def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A
    '''
    print("\033[{};{}H".format(x, y), end='', flush=True)

def add(cdl, size, emojis):
    item = input("What do you want to add?\n>>")
    while item not in emojis:
        if size == 1:
            print_location(19,1, "What do you want to add?\n>>"+" "*20 )
            move_cursor(20,3)
            item = input()
        else:
            print_location(20,1, "What do you want to add?\n>>"+" "*20)
            move_cursor(21,3)
            item = input()
    dir = input("On which side do you want to add emoji frame? (left/ right): ").lower()
    while dir != "left" and dir!="right":
        if size == 1:
            print_location(21,1, "On which side do you want to add emoji frame? (left/ right): "+" "*20)
            move_cursor(21, 62)
            dir = input().lower()
        else:
            print_location(23,1, "On which side do you want to add emoji frame? (left/ right): "+" "*20)
            move_cursor(22, 62)
            dir = input().lower()
    if dir == "right":
        if size == 1:
            art.addRightInitial()
        else:
            l = emojis[cdl.current.prev.data]
            r = emojis[cdl.current.next.data]
            art.addRight(l, r)
        cdl.addRight(item)
    elif dir == "left":
        if size == 1:
            art.addLeftInitial()
        else:
            l = emojis[cdl.current.prev.data]
            r = emojis[cdl.current.next.data]
            art.addLeft(l, r)
        cdl.addLeft(item)

def move(cdl, dir):
    if dir.lower() == "l":
        cdl.getLeft()
    else:
        cdl.getRight()
def delete(cdl, size):
    l = emojis[cdl.current.prev.data]
    r = emojis[cdl.current.next.data]
    if size == 1:
        art.deleteInitial()
    else:
        art.delete(l, r)
    cdl.deleteCurrent()

    return size-1
    
def info(cdl, original_data):
    obj = cdl.current.data
    sym = emojis[obj]
    Class = None
    if obj in original_data[0]["emojis"]:
        Class = "food"
    else:
        Class = "animals"
    print(f"Objecct: {obj}")
    print(f"Sym: {sym}")
    print(f"Class: {Class}\n")
    n = input("Click any Button to continue ")

def begin(cdl, emojis):
    print("Type any of the following commands to perform the action:")
    print(" "*8 + "ADD: Add a emoji frame")
    print(" "*8 + "Q: Quit the program")
    action = input(">> ")
    if action.lower() == "add":
        item = input("What do you want to add?\n>> ")
        while item not in emojis:
            print_location(5,1, "What do you want to add?")
            print_location(6,1, " "*20)
            move_cursor(6,1)
            item = input(">>")
        cdl.add(item)
    elif action.lower() == "q":
        return "quit"
    else:
        return "invalid"

with open('emojis.json', 'r', encoding='utf-8') as file:
    original_data = json.load(file)
emojis = [i['emojis'] for i in original_data]
emojis = {**emojis[0], **emojis[1]} #combining both dictionaries
quit = False
cdl = CircularDoublyLinkedList()
size = 0
while not quit:
    if size == 0:
        clear_screen()
        q = begin(cdl, emojis)
        if q == "quit":
            quit = True
        elif q == "item not found":
            print("Item not found")
            continue
        elif q == "invalid":
            continue
        else:
            emoji = emojis[cdl.current.data]
            art.start(emoji)
        size+=1
        continue
    time.sleep(0.5)
    clear_screen()
    current = cdl.current
    i = emojis[current.data]
    if size > 1:
        previous = cdl.current.prev
        next_n = cdl.current.next
        l = emojis[previous.data]
        r = emojis[next_n.data]
        art.display(i, l, r)
        print("Type any of the following commands to perform the action:")
        print(" "*8 + "L: Move Left")
        print(" "*8 + "R: Move Right")
    else:
        art.initial(i)
        print("Type any of the following commands to perform the action:")
    print(" "*8 + "ADD: Add a emoji frame")
    print(" "*8 + "DEL: Delete current emoji frame")
    print(" "*8 + "INFO: Retrieve info about current frame")
    print(" "*8 + "Q: Quit the program")
    action = input(">>")
    if action.lower() == "l" or action.lower() == "r":
        move(cdl, action)
    if action.lower() == "add":
        add(cdl, size, emojis)
        size+=1
    elif action.lower() == "del":
        s = delete(cdl, size)
        size = s
    elif action.lower() == "info":
        info(cdl, original_data)
    elif action.lower() == "q":
        quit = True
    else:
        continue
    
    