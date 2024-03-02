#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    Write docstring to describe function
    Inputs: __
    Returns: action
    '''
    req = ["=", "<", ">", "q"]
    action = input("Enter = to enter a URL, < to go back, > to go forward, q to quit:")
    if action not in req:
        raise Exception("Invalid Entry")
    
    return action

def goToNewSite(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: current, bck, fwd
    Returns: url
    '''   
    url = input("URL: ")
    bck.push(current)
    fwd.clear()
    return url
    
def goBack(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: current, bck, fwd
    Returns: current -> previous website
    '''    
    if not bck.isEmpty():
        fwd.push(current)
        current = bck.pop()
    else:
        print("Cannot go back")
    return current

def goForward(current, bck, fwd):
    '''
    Write docstring to describe function
    Inputs: current, bck, fwd
    Returns: current -> forward
    '''    
    if not fwd.isEmpty():
        bck.push(current)
        current = fwd.pop()
    else:
        print("cannot go forward")
    return current

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try:
            action = getAction()
            
        except Exception as actionException:
            print(actionException.args[0])
            
        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    