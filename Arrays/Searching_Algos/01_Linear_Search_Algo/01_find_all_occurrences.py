"""
Problem : Find all occurrences

Return a list containing every index where the target appears.

arr = [20, 74, 98, 74, 65, 74]
target = 74
"""

import array

arr = array.array('i',[20, 74, 98, 74, 65, 74])
target = 74


def get_trg_indx_lst(arr, target):

    lst_idx = array.array('i', [])

    for  i in range(len(arr)):

        if arr[i] == target:
            lst_idx.append(i)

    if len(lst_idx) != 0:
        return lst_idx.tolist()
    
    else:
        return -1
    
print(get_trg_indx_lst(arr, target))