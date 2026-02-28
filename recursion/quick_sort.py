# quick sort 

class Solution():
  
  def partion(self, arr, start, end):
    idx = start - 1
    pivot = arr[end]

    for j in range (start, end):
      if pivot >= arr[j]:
        idx += 1
        arr[idx], arr[j] = arr[j], arr[idx]
       

    idx+=1
    arr[idx], arr[end] = arr[end], arr[idx]

    return idx


  def Quicksort(self, arr, start, end):

    if start < end:
      pivot_idx = self.partion(arr, start, end)
      self.Quicksort(arr,start, pivot_idx - 1  ) # left side quick sort
      self.Quicksort(arr,pivot_idx + 1, end  ) # right side quick sort 






sol = Solution()
arr = [1,9,3,2,5,7]
sol.Quicksort(arr, 0, len(arr)-1)
print(arr)


