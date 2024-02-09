#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

def getAction():
    '''
    Write docstring to describe function
    Inputs: None
    Returns: string value (action required)
    '''
    req = ["=", "<", ">", "q"]
    action = input("Enter = to enter a URL, < to go back, > to go forward, q to quit:")
    if action not in req:
        print("Invalid entry")
        getAction()
    else:
        return action

def goToNewSite(current, pages):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''   
    l = len(pages)
    url = input("URL: ")
    if current != (l-1):
        for i in range(current+1, l):
            pages.pop(current+1)#as the list keeps on getting shorter
    pages.append(url)
    return pages.index(url)

    
def goBack(current, pages):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    if current == 0:
        print("Cannot go back")
    else:
        current -= 1
    return current


def goForward(current, pages):
    '''
    Write docstring to describe function
    Inputs: ?
    Returns: ?
    '''    
    if current == len(pages) - 1:
        print("Cannot go forward")
    else:
        current+=1
    return current


def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    