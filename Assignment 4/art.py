import os
"""
                             ↓↓
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   |                            |   |          
           |   |                            |   |          
 ()        |   |             ()             |   |        ()
           |   |                            |   |          
 __________|   |                            |   |__________
               |____________________________|

"""

"""
                             ↓↓
               |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    
               |                            |          
               |                            |        
               |             ()             |       
               |                            |         
               |                            |  
               |____________________________|

                             
"""

"""
                             /\ 
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   |           /    \           |   |                   
           |   |          /_    _\          |   |                   
 ()        |   |            |  |            |   |        ()        
           |   |            |  |            |   |                  
 __________|   |            |  |            |   |__________
               |____________|  |____________|
                            |__|
"""

"""
                             /\ 
               |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|   
               |           /    \           |                    
               |          /_    _\          |           
               |            |  |            |       
               |            |  |            |                  
               |            |  |            |   
               |____________|  |____________|
                            |__|
                             
"""

"""
                                         |\
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
           |   |                         |  \   |                   
           | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
 ()        | |            Right               | |        ()        
           | |___________________________    /  |                  
 __________|   |                         |  /   |__________
               |_________________________| /
                                         |/
"""

"""
                                         |\
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
           |   |                         |  \   |                   
           | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
 ()        | |        Adding Right            | |        ()        
           | |___________________________    /  |                  
 __________|   |                         |  /   |__________
               |_________________________| /
                                         |/
                             
"""

"""
                                         |\
               |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \  
               |                         |  \          
             |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \          
             |        Adding Right            |    
             |___________________________    /    
               |                         |  /  
               |_________________________| /
                                         |/
                             
"""

"""
                 /|                      
 __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   /  |                         |   |                   
           |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
 ()        | |              Left              | |        ()        
           |  \    ___________________________| |                  
 __________|   \  |                         |   |__________
                \ |_________________________|
                 \|                      
""" 

"""
                 /|                      
 __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   /  |                         |   |                   
           |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
 ()        | |           Adding Left          | |        ()        
           |  \    ___________________________| |                  
 __________|   \  |                         |   |__________
                \ |_________________________|
                 \|                      
                             
"""

"""
                 /|                      
                / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   
               /  |                         |          
              /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|      
             |           Adding Left          |       
              \    ___________________________|             
               \  |                         |   
                \ |_________________________|
                 \|                      
                             
"""

"""
                            |‾‾|
               |‾‾‾‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾‾‾‾|   
               |            |  |            |                   
               |            |  |            |                    
               |           _|  |_           |   
               |          \      /          |                
               |           \    /           |   
               |____________\  /____________|
                             \/
                            
"""
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

def start(i):
    clear_screen()
    print(
"""
                            |‾‾|
               |‾‾‾‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾‾‾‾|   
               |            |  |            |                   
               |            |  |            |                    
               |           _|  |_           |   
               |          \      /          |                
               |           \    /           |   
               |____________\  /____________|
                             \/
                            
""" )

def initial(i):
    print(
f"""
                             ↓↓
               |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    
               |                            |          
               |                            |        
               |            {i}              |       
               |                            |         
               |                            |  
               |____________________________|

                             
"""
      
    )

def addRightInitial():
    clear_screen()
    print(
"""
                                         |\
               |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \  
               |                         |  \          
             |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \          
             |        Adding Right            |    
             |___________________________    /    
               |                         |  /  
               |_________________________| /
                                         |/
                             
"""   
    )
def addLeftInitial():
    clear_screen()
    print(
"""
                 /|                      
                / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   
               /  |                         |          
              /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|      
             |           Adding Left          |       
              \    ___________________________|             
               \  |                         |   
                \ |_________________________|
                 \|                      
                             
"""
    )
def addLeft(l, r):
    clear_screen()
    print(
f"""
                 /|                      
 __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   /  |                         |   |                   
           |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
  {l}      | |           Adding Left          | |       {r}        
           |  \    ___________________________| |                  
 __________|   \  |                         |   |__________
                \ |_________________________|
                 \|                      
                             
"""
    )

def addRight(l, r):
    clear_screen()
    print(
f"""
                                         |\
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
           |   |                         |  \   |                   
           | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
 {l}       | |        Adding Right            | |       {r}        
           | |___________________________    /  |                  
 __________|   |                         |  /   |__________
               |_________________________| /
                                         |/
                             
"""
    )
def goLeft(l, r):
    clear_screen()
    print(
f"""
                 /|                      
 __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   /  |                         |   |                   
           |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
  {l}      | |              Left              | |       {r}        
           |  \    ___________________________| |                  
 __________|   \  |                         |   |__________
                \ |_________________________|
                 \|                      
""" 
    )

def goRight(l, r):
    clear_screen()
    print(
f"""
                                         |\
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
           |   |                         |  \   |                   
           | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
 {l}       | |            Right               | |        {r}        
           | |___________________________    /  |                  
 __________|   |                         |  /   |__________
               |_________________________| /
                                         |/
"""
    )

def display(i, l, r):
    print(
f"""
                             ↓↓
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   |                            |   |          
           |   |                            |   |          
  {l}       |   |            {i}              |   |     {r}
           |   |                            |   |          
 __________|   |                            |   |__________
               |____________________________|

"""
    )
    
def delete(l, r):
    clear_screen()
    print(
f"""
                             /\ 
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   |           /    \           |   |                   
           |   |          /_    _\          |   |                   
 {l}        |   |            |  |            |   |       {r}        
           |   |            |  |            |   |                  
 __________|   |            |  |            |   |__________
               |____________|  |____________|
                            |__|
"""

    )
def deleteInitial():
    clear_screen()
    print(
"""
                             /\ 
               |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|   
               |           /    \           |                    
               |          /_    _\          |           
               |            |  |            |       
               |            |  |            |                  
               |            |  |            |   
               |____________|  |____________|
                            |__|
                             
"""       
    )