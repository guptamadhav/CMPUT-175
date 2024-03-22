from bqueue import BoundedQueue
from bstack import Stack
import os
import time

os.system("")  # enables ANSI characters in terminal

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

def  chemicals_data():
    with open("chemicals.txt", mode="r") as f:
        data = f.readlines()
        data = [i[:-1] if i[-1] == "\n" else i for i in data]
    return data

def build(data):
    """
    takes in data. build a queue as suggested and then transfer into flasks
    """
    m = int(data[0].strip()[0])
    flasks = {}
    for i in range(m):
        flask_name = f"flask{i+1}"
        flasks[flask_name] = Stack()
    chemicals_queue = BoundedQueue(4)
    for i in data[1:]:
        if i[1] == "F" and len(i) == 3:
            m,n = map(int, i.split("F"))
            for j in range(m):
                try:
                    chem = chemicals_queue.dequeue()
                except Exception as dequeueError:
                    pass
                try:
                    flasks[f"flask{n}"].push(chem)
                except Exception as pushError:
                    pass
        else:
            try:
                chemicals_queue.enqueue(i)
            except Exception as enqueueError:
                pass
    return flasks

def print_flasks(flasks):
    reset = "\033[49m"
    color = {
        "AA" : "\033[41m",
        "BB" : "\033[44m",
        "CC" : "\033[42m",
        "DD" : "\033[48;5;208m",
        "EE" : "\033[43m",
        "FF" : "\033[45m"
        }
    for i in range(3,-1,-1):#in order to get elements of stack from top to bottom
        flask_i = ""
        for j in range(len(flasks)):
            if j<4:
                items = flasks[f"flask{j+1}"].items
                if isFull(items) and i==3:
                    flask_i += "+--+  "
                else:
                    try:
                        chem = color[items[i]] + items[i] + reset
                        flask_i += ("|"+chem+"|  ")
                    except IndexError:
                        flask_i += "|  |  "
            else:
                break
        print(flask_i)
    if len(flasks)<4:
        end_line = "+--+  "*len(flasks)
    else:
         end_line = "+--+  "*4
    num = [f"  {i+1}  "  for i in range(min(len(flasks), 4))]
    print(end_line)
    print(" ".join(num) + "\n")
    if len(flasks)>4:
        for i in range(3,-1,-1):#in order to get elements of stack from top to bottom
            flask_i = ""
            for j in range(4, len(flasks)):
                items = flasks[f"flask{j+1}"].items
                if isFull(items) and i==3:
                    flask_i += "+--+  "
                else:
                    try:
                        chem = color[items[i]] + items[i] + reset
                        flask_i += ("|"+chem+"|  ")
                    except IndexError:
                        flask_i += "|  |  "
            print(flask_i)
        end_line = "+--+  "*(len(flasks)-4)
        num = [f"  {i+1}  "  for i in range(4, len(flasks))]
        print(end_line)
        print(" ".join(num))

def isFull(items):
    if len(items) == 3 and all(i == items[0] for i in items):
        return True
    else:
        return False
    
def complete(flasks):
    allDone = []
    for i in range(len(flasks)):
        items = flasks[f"flask{i+1}"].items
        full = isFull(items)
        if flasks[f"flask{i+1}"].isEmpty():
            allDone.append("True")
        else:
            allDone.append(full)
    if any(i == False for i in allDone):
        return False
    else:
        return True

def source(flasks):
    m = int(input())
    if m>len(flasks) or flasks[f"flask{m}"].isEmpty():
        print_location(5, 1,"Invalid Flask")
        print_location(3, 21, " ")
        move_cursor(3,21)
        return source(flasks)
    items = flasks[f"flask{m}"].items
    if isFull(items):
        print_location(5, 1, "The flask is sealed")
        print_location(3, 21, " ")
        move_cursor(3,21)
        return source(flasks)
    else:
        return m

def destination(m, flasks):
    n = int(input())
    if n>len(flasks):
        print_location(5, 1, "Invalid Flask")
        print_location(4, 26, " ")
        move_cursor(4, 26)
        return destination(m, flasks)
    items = flasks[f"flask{n}"].items
    if isFull(items) or flasks[f"flask{n}"].isFull():
        print_location(5, 1, "Cannot pour into that flask. Try again.")
        print_location(4, 26, " ")
        move_cursor(4, 26)
        return destination(m, flasks)
    elif m==n:
        print_location(5, 1, "Cannot pour into same flask. Try again")
        print_location(4, 26, " ")
        move_cursor(4, 26)
        return destination(m, flasks)
    else:
        return n

def pour(m, n, flasks):
     chem = flasks[f"flask{m}"].pop()
     flasks[f"flask{n}"].push(chem)

data = chemicals_data()
flasks = build(data)
win = False
while not win:
    clear_screen()
    print("Magical Flask Game")
    print("\nSelect Source flask: ")
    print("Select Destination Flask: \n" ) 
    print_flasks(flasks)
    move_cursor(3, 21)
    m = source(flasks)
    move_cursor(4, 26)
    n = destination(m, flasks)
    pour(m, n, flasks)
    if complete(flasks):
        print_location(5,1, "                                               ")
        (print_flasks(flasks))
        if len(flasks)<=4:
            print_location(12,1,"You win!")
        else:
            print_location(19,1, "You win")
        win = True
    
    