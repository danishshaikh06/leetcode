'''Single Element in a Sorted Array
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
'''
from typing import List

class Solution:
    def single(self, nums: List[int]):
        # If there's only one element, that's the single element
        if (len(nums) == 1):
            return nums[0]
        
        # If the first element is different from the next one,
        # it means the first element is the single one
        if (nums[0] != nums[1]):
            return nums[0]
        
        # If the last element is different from the previous one,
        # it means the last element is the single one
        if (nums[-1] != nums[-2]):
            return nums[-1]
        
        # Initialize binary search boundaries
        start, end = 1 , len(nums) - 2
        
        # Perform binary search to find the single element
        while start <= end:
            mid = (start + end) // 2

            # If nums[mid] is not equal to either neighbor,
            # this is the single element
            if (nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]):
                return nums[mid]
            
            # Now, determine which side of the array the single element is on.
            # Here's the key insight:
            # - In a properly paired array (sorted), pairs appear as [even, odd] indices.
            # - Before the single element, pairs start at even indices (0,2,4,...)
            # - After the single element, pairs start at odd indices (1,3,5,...)

            # So we check:
            # Case 1: mid is odd and equals previous → single element is on the right side
            # Case 2: mid is even and equals next → single element is on the right side
            if (mid % 2 == 1 and nums[mid] == nums[mid-1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                start = mid + 1  # search right half
            else:
                end = mid - 1    # search left half

        # If not found (shouldn't happen for valid input)
        return -1

    
sol = Solution()
nums = [1,1,2,3,3,4,4,8,8] 
result = sol.single(nums)
print(result)

