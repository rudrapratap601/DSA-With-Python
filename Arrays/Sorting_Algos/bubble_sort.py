def bubble_sort(arr: list, ascending = True) -> list:
    """This function will sort the array ascending to descending"""
    n = len(arr)

    if ascending:
        for i in range(n):
            for j in range(n - 1):
        
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    else:
         for i in range(n):
              for j in range(n - 1):

                  if arr[j] < arr[j + 1]:
                      arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr



arr = [12, 11, 25, 34, 22, 90]
print(arr)

sorted_arr = bubble_sort(arr, ascending = False) 
print(sorted_arr)