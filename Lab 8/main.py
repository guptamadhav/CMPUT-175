def my_len(some_list):
    if len(some_list) == 1:
        return 1
    else:
        some_list.pop()
        return 1 + my_len(some_list)

def intDivision(divident, divisor):
    if divident<divisor:
        return 0
    else:
        return 1 + intDivision(divident - divisor, divisor)

def sumDigits(num):
    num = int(num)
    if num<10:
        return num
    else:
        return num%10 + sumDigits(num/10)

def reverseDisplay(num):
    num = int(num)
    if num<10:
        return str(num)
    else:
        return str(num%10) + reverseDisplay(num/10)

def binary_search1(key,alist,low,high):
    # finds and returns the position of key in alist
    # or returns ‘Item is not in the list’
    # - key is the target integer that we are looking for
    # - alist is a list of valid integers that is searched
    # - low is the lowest index of alist
    # - high is the highest index of alist
    if low<high:
        return -1
    guess = (high+low)//2
    if (key == alist[guess]):
        return guess   
    elif (key < alist[guess]):
        return binary_search1(key, alist, low, guess - 1)
    else:
        return binary_search1(key, alist, guess + 1, high)
    

number = int(input('Enter a number:'))
print(reverseDisplay(number))