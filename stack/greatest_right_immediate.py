def gratest(arr):
    stack = []
    ans = [0] * len(arr)

    for i in range(len(arr)-1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()

        if not stack:
            ans[i] = -1
        else:
            ans[i] = arr[stack[-1]]

        stack.append(i)

    return ans

# Example usage
arr = [4, 5, 2, 10, 8]
print(gratest(arr))  # Output: [5, 10, 10, -1, -1]