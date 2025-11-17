from typing import List

class Solution:
    def mountain(self, nums: List[int]):  
        # Edge case: only one element in the array
        if len(nums) == 1:
            return nums[0]

        # Edge case: first element is the peak
        if nums[0] > nums[1]:
            return nums[0]

        # Edge case: last element is the peak
        if nums[-1] > nums[-2]:
            return nums[-1]
        
        # Initialize binary search pointers
        start, end = 1, len(nums) - 2

        while start <= end:
            mid = start + (end - start) // 2  # Find middle index

            # Check if mid is the peak
            # A peak is greater than its immediate neighbors
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return nums[mid]  # Found the peak

            # Decide which side to search next
            if nums[mid] > nums[mid + 1]:
                # If mid is greater than mid+1, peak is on the left side (including mid)
                end = mid - 1
            else:
                # If mid is smaller than mid+1, peak is on the right side
                start = mid + 1

        # If no peak found (should not happen in a proper mountain array)
        return -1


# Example usage
sol = Solution()
nums = [1, 3, 5, 4, 2]
result = sol.mountain(nums)
print(result)  # Output: 5

