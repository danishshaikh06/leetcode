'''Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
A subarray is a contiguous non-empty sequence of elements within an array.

Examples:
Input: nums = [2, 3, 5, -2, 7, -4]
Output: 15
Explanation:
The subarray from index 0 to index 4 has the largest sum = 15

Hint:
It is Solved using kadane's algo where condition states that if (sum< 0) dont add it to sum'''
from typing import List
class Solution:
    def max_sub_array_sum(self, nums: List[int]): 
        maximum =nums[0]
        large = 0 
        start = 0
        end = 0
        temp_start = 0
        for i in range(len(nums)):
            large = large + nums[i]
            if (large < 0):
                large = 0
                temp_start = i + 1
            elif (large > maximum):
                maximum = large
                start = temp_start
                end = i

        max_subarr = nums[start : end+1]
    
        return maximum, max_subarr
    
sol = Solution()
nums = [2, 3, 5, -2, 7, -4]
result = sol.max_sub_array_sum(nums)
print(result)
 
