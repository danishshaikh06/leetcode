'''Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation. 

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]'''

from typing import List
class Solution:
    def array_product(self, nums: List[int]):
        prefix = []
        curr_1 = nums[0]
        suffix = nums[-1]
        product = 0

        for i in range(len(nums)):
            curr_1 = curr_1 * nums[i-1] if i > 0 else 1
            prefix.append(curr_1) # prefix product array [1,1,2,6]
        
        for j in range(len(nums)-1, -1, -1):
            suffix = suffix * nums[j + 1] if j < len(nums) - 1 else 1
            product = suffix * prefix[j]
            prefix[j] = product  # final product array [24,12,8,6]

        return prefix
        
sol = Solution()
nums = [1,2,3,4]
result = sol.array_product(nums)
print(result)