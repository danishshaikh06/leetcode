def binary_search(arr, target, start, end):
    if start > end:
        return -1  

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)


array = [1, 2, 3, 4, 5, 6, 7]
target = 5

result = binary_search(array, target, 0, len(array) - 1)
print("Target index:", result)