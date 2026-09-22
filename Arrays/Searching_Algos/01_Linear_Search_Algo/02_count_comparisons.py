"""
Problem : Count Comparisons

Count how many comparisons the algo performs before finding the target

arr = [20, 98, 74, 65, 82, 74] 
target = 65
"""

import array


def count_comp(arr, target):

    count_comparisons = 0

    for i in range(len(arr)):
        count_comparisons += 1
        if arr[i] == target:
            return f"index : {i}\nComparisons : {count_comparisons}"
    else:
        return -1

arr = array.array('i', [20, 98, 74, 65, 82, 74])
target = 65

print(count_comp(arr, target))