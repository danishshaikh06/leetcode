from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2  # Find middle index

            if nums[mid] == target:
                return mid  # Target found, return its index

            # Determine which half is properly sorted
            if nums[start] <= nums[mid]:
                # Left half [start...mid] is sorted
                if nums[start] <= target < nums[mid]:
                    end = mid - 1  # Target is in left half, move end
                else:
                    start = mid + 1  # Target not in left half, search right half
            else:
                # Right half [mid...end] is sorted
                if nums[mid] < target <= nums[end]:
                    start = mid + 1  # Target is in right half, move start
                else:
                    end = mid - 1  # Target not in right half, search left half

        return -1  # Target not found


"""
Detailed Explanation:

This function searches for a target in a rotated sorted array using modified binary search. 

Key ideas:

1. Rotated Sorted Array:
   - A rotated sorted array is a sorted array that has been rotated at some pivot.
   - Example: original [0,1,2,4,5,6,7] rotated → [4,5,6,7,0,1,2]

2. Binary Search Principle:
   - Normally, binary search works on a fully sorted array.
   - Here, because of rotation, one half is always sorted.
   - We can determine the sorted half and decide which half to search.

3. Step-by-Step Logic:
   - Calculate mid = (start + end) // 2
   - If nums[mid] == target → return mid immediately
   - Check which half is sorted:
       a) Left half sorted if nums[start] <= nums[mid]
       b) Right half sorted if nums[mid] <= nums[end] (else)
   - Determine if target lies in the sorted half:
       - If yes, continue searching in that half
       - If no, search in the other half
   - Repeat until start > end (target not found)

4. Why it works:
   - Each iteration halves the search space (like standard binary search)
   - Even with rotation, one half is guaranteed sorted, allowing us to decide which half to discard

5. Time Complexity: O(log n)
   - Each iteration reduces the search interval by half

6. Space Complexity: O(1)
   - No extra space is used, only variables start, end, mid
"""
