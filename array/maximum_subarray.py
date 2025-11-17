'''Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [2,-3,4,-2,2,1,-1,4]
Output: 8'''


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize both to the first element
        maxsub = nums[0]
        currsum = nums[0]

        # Iterate through remaining elements
        for n in nums[1:]:
            # Either start new subarray at n, or extend existing one
            currsum = max(n, currsum + n)
            
            # Update max found so far
            maxsub = max(maxsub, currsum)

        return maxsub
    

    

        