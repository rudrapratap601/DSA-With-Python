import array

"""Writing Algorithm for Linear Search"""

def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    else:
        return -1




arr = array.array('i', [20, 98, 74, 65, 82, 74])
target = 65

print(linear_search(arr, target))

"""
Time and space complexity

Case           |  Complexity   |  Explanation

Best case      |  O(1)   |  Target is at index 0.
Average case  |  O(n)   |   The algorithm examines a number of elements proportional to the array size, on average.
Worst case   | 	O(n)   |    Target is at the last index or is absent.

Auxiliary space  |  O(1) | The algorithm uses a constant amount of extra memory.

"""