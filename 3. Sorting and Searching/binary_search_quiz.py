"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

import math

def binary_search(input_array, value):
    """Your code goes here."""
    result = 0
    while True :
        if (len(input_array) % 2)== 0 :
            middle_index = int((len(input_array)/2))
        if (len(input_array) % 2)!= 0 :
            middle_index = int(math.floor(len(input_array)/2))+1
        middle_value = input_array[middle_index]
        if middle_value == value :
            result = result + middle_index
            break
        if middle_value < value : 
            input_array = input_array[middle_index:]
            result = result + middle_index
        if middle_value > value : 
            input_array = input_array[:middle_index]
            result = result - middle_index
        if len(input_array) == 1 :
            result = -1
            break
        
    return result

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))