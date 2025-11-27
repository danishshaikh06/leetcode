'''18. 4Sum
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]'''


from typing import List
class Solution:
    def four_sum(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        ans = []

        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                l, r = j + 1, n - 1

                while l < r:
                    s = arr[i] + arr[j] + arr[l] + arr[r]

                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1         
                    else:
                        ans.append([arr[i], arr[j], arr[l], arr[r]])
                        l += 1
                        r -= 1

                        while l < r and arr[l] == arr[l - 1]:
                            l += 1
                        while l < r and arr[r] == arr[r + 1]:
                            r -= 1

        return ans
 

