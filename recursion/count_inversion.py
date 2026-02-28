# count inversion 

class Solution():
  def merge(self, arr, start, mid, end):
    i = start
    j = mid + 1
    temp = []
    count = 0

    while i <= mid and j <= end:
      if arr[i] < arr[j]:
        temp.append(arr[i])
        i+=1
      else:
        temp.append(arr[j])
        count += (mid - i + 1)
        j+=1
        
    while i<=mid:
      temp.append(arr[i])
      i+=1

    while j<=end:
      temp.append(arr[j])
      j+=1

    for k in range (len(temp)):
      arr[start + k] = temp[k]

    return count 

  def mergesort(self, arr, start , end):

    if start < end:

      mid = (start + end ) // 2
      left_count = self.mergesort(arr, start, mid) # left
      right_count = self.mergesort(arr, mid + 1, end) # right
      count = self.merge(arr, start, mid, end)

      return left_count + right_count  + count
    
    return 0

sol = Solution()
arr = [6,3,5,2,7]
print(sol.mergesort(arr, 0, len(arr)-1))

