'''11. Container With Most Water
Hint
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.'''

from typing import List

class Solution:
    def most_water(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        max_area = 0

        while l < r:
            h = min(nums[l], nums[r])
            w = r - l
            area = h * w
            if area > max_area:
                max_area = area

            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1

        return max_area

# Example
sol = Solution()
nums = [1,8,6,2,5,4,8,3,7]
result = sol.most_water(nums)
print("Maximum water can be stored is:", result)  # prints 49
