'''560. Subarray Sum Equals K
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2'''

from typing import List
class Solution:
    def len_array(self, nums: List[int], k: int):
        Sum = 0
        count = 0
        for i in nums:
            Sum = Sum + i
            if (Sum == k or Sum - k == 0 ):
                count +=1
            elif (Sum - k == k):
                count+=1

        return count
    
sol = Solution()
nums = [1,1,1]
k = 2
result = sol.len_array(nums , k)
print (result)

    


