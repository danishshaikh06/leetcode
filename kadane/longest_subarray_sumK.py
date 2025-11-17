'''Longest subarray with sum K

Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.

Examples:
Input: nums = [10, 5, 2, 7, 1, 9],  k=15
Output: 4

Explanation:
The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.'''

from typing import List

class Solution:
    def longest_subarray(self, nums: List[int], k: int):
        Sum = 0
        l, r = 0, 0
        max_len = 0
        count = 0
        sub_array = []
        

        while r < len(nums):
            Sum += nums[r]

            if Sum == k:
                count +=1
                sub_array.append(nums[l:r+1])
                max_len = max(max_len, r - l + 1)
                
            while Sum > k and l <= r:
                Sum -= nums[l]
                l += 1

            r += 1  

        return max_len, count,sub_array



sol = Solution()
k = 15
nums = [10, 5, 2, 7, 1, 9]
max_len, count ,sub_array= sol.longest_subarray(nums, k)
print("Longest subarray length:", max_len)
print("subarray equal to k:", sub_array)
print("Count of subarray equal to k:", count)


                






