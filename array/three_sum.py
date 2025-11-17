'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort so we can use two pointers and skip duplicates easily
        nums.sort()
        res = []

        # i goes from 0 .. len(nums)-1; we'll use l=i+1 and r=end
        for i, n in enumerate(nums):
            # Skip duplicate first elements (prevents duplicate triplets)
            if i > 0 and n == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            # two-pointer search for two numbers that sum to -n
            while l < r:
                # === BUG FIX: use + not - ===
                curr_sum = n + nums[l] + nums[r]

                if curr_sum > 0:
                    # sum too big -> move right pointer left
                    r -= 1
                elif curr_sum < 0:
                    # sum too small -> move left pointer right
                    l += 1
                else:
                    # === BUG FIX: append a list of three values ===
                    res.append([n, nums[l], nums[r]])

                    # move both pointers to continue searching
                    l += 1
                    r -= 1   # === BUG FIX: r should decrease, not "r =+ 1" ===

                    # skip duplicates for left pointer (so we don't produce same triplet)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # skip duplicates for right pointer
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res


# Example usage and printing the results
sol = Solution()
nums = [1, 2, 2, -3, 3, 4, 9]
result = sol.threeSum(nums)
print("input:", nums)
print("triplets summing to 0:", result)
