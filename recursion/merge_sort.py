class Solution():
    def merge(self, arr, start, mid, end):
        i = start
        j = mid + 1
        temp = []

        while i <= mid and j <= end:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i <= mid:
            temp.append(arr[i])
            i += 1

        while j <= end:
            temp.append(arr[j])
            j += 1

        # Copy merged elements back into original array
        for k in range(len(temp)):
            arr[start + k] = temp[k]

    def divide(self, arr, start, end):
        if start < end:
            mid = (start + end) // 2
            self.divide(arr, start, mid) # left
            self.divide(arr, mid + 1, end) # right
            self.merge(arr, start, mid, end)

        return arr
