
def binary_search(arr, target):

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (end + start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    else :
        return -1


arr = [21, 34, 49, 68, 89, 93]
target = 93

print(binary_search(arr, target))


"""
Time and space complexity

Case           |  Complexity   |  Explanation

Best case      |  O(1)   |  Target is at index 0.
Average case  |  O(log n)   |   The algorithm examines a number of elements proportional to the array size, on average.
Worst case   | 	O(log n)   |    Target is at the last index or is absent.

Auxiliary space  |  O(1) | The algorithm uses a constant amount of extra memory.
"""