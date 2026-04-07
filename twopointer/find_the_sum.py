arr = [1,3,4,6,7]
left = 0
right = len(arr) - 1
target = 10

while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == target:
        print(f"Pair found: {arr[left]} and {arr[right]}")
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1