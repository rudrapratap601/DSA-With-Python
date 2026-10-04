def selection_sort(arr: list) -> list:
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [12, 11, 25, 34, 22, 90]
print(arr)

sorted_arr = selection_sort(arr) 
print(sorted_arr)
