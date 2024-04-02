import random
import time

#---------------------------------------#      
# Implement Recursive selection sort here. 

# n: size of array - index is index of starting element
def recursive_selection_sort(data, data_len, index = 0): 
  
    # TODO-Remove pass and fill out the rest. 
    #You may use additional user_defined functions if required.
    # sorted in descending order
    # Set the base case 
    if data_len==1:
        return data
    else:
    # Find the minimum index 
        for i in range(1,data_len):
            if data[i] < data[index]:
                index = i      
        # Swap the data, minimum value is assigned to las 
        data[index],data[data_len-1] = data[data_len-1], data[index]      
        # Recursively calling selection sort function 
        return recursive_selection_sort(data, data_len-1)
#---------------------------------------#
#Implement the Recursive merge sort here
  
def recursive_merge_sort(data): 
    
    # TODO-Remove pass and fill out the rest. 
    #You may use additional user_defined functions if required.

    # Set the base case 
    if len(data)<=1:
        return data
    #Find the middle of the data list
    midpoint = len(data)//2 
    #Recursively calling merge sort function for both half of the data list
    left_half = recursive_merge_sort(data[:midpoint])
    right_half = recursive_merge_sort(data[midpoint:])   
    # merge the two halves of the data list and return the data list
    return MergeSort(left_half, right_half)

def MergeSort(left_half, right_half):
    result = []
    while len(left_half)>0 and len(right_half)>0:
        if left_half[0]>right_half[0]:
            result.append(left_half[0])
            left_half.pop(0)
        else:
            result.append(right_half[0])
            right_half.pop(0)
    result += left_half
    result += right_half
    return result
#----------------
# -----------------------#
if  __name__== "__main__":
    # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
      
    # Calculate the execution time to sort a list of random numbers #
    random_list_ = random_list.copy()  # make a copy to save the unsorted list
    start_sel = time.time()
    recursive_selection_sort(random_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
    
    
    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    ascending_list_ = ascending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(ascending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in ascending order 
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))      
    
    
    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    descending_list_ = descending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(descending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
