"""
Problem : Find the Maximum Element

CUsing a linear scan, find the largest element in an array without using Python's built-in max() function.

arr = [20, 98, 74, 65, 82, 74]
"""

import array 

def find_max(arr):

    max_ele = arr[0]

    for i in range(1, len(arr)):
        if max_ele < arr[i]:
            max_ele = arr[i]

    return max_ele

arr = array.array('i', [20, 98, 74, 65, 182, 74])

print(find_max(arr))