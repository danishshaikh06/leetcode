'''Aggressive Cows
Given an array nums of size n, which denotes the positions of stalls, and an integer k, which denotes the number of aggressive cows, assign stalls to k cows such that the minimum distance between any two cows is the maximum possible. Find the maximum possible minimum distance.

Examples:
Input: n = 6, k = 4, nums = [0, 3, 4, 7, 10, 9] # sorted-> [0,3,4,7,9,10]
Output: 3
Explanation: The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions [0, 3, 7, 10]. Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.'''
from typing import List
class Solution:
    def count_cows(self, nums: List[int], dist: int, cows: int):
        count = 1 
        last = nums[0]
        for i in range (1 , len(nums)):
            if (nums[i] - last >= dist):
                count+=1
                last = nums[i]
            if count >= cows:
                return True      
        return False
           
    def agressive_cows(self, nums: List[int], k: int):
        nums.sort()
        low = 1
        high = nums[-1] - nums[0] 
        result = 0
        while (low <= high):
            mid = (low + high) // 2
            if (self.count_cows(nums, mid, k)):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result
    
sol = Solution()
k = 4
nums = [0, 3, 4, 7, 10, 9]
result = sol.agressive_cows(nums, k)
print (result, nums)

