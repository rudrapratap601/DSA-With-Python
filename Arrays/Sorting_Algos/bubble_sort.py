def bubble_sort(arr: list, ascending = True) -> list:
    """This function will sort the array ascending to descending"""
    n = len(arr)

    if ascending:
        for i in range(n):
            is_swap = False     
            for j in range(n - 1 - i):
        
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    is_swap = True

            if is_swap == False:
                return arr
    else:
         for i in range(n):
            is_swap = False
            for j in range(n - 1):

                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    is_swap = True

            if is_swap == False:
                return arr
                

    return arr

arr = [12, 11, 25, 34, 22, 90]
print(arr)

sorted_arr = bubble_sort(arr) 
print(sorted_arr)