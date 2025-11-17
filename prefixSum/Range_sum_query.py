''''Prefix Sum involves preprocessing an array to create a new array where each element at index i represents the sum of the array from the start up to i. This allows for efficient sum queries on subarrays.

When to use -> Use this pattern when you need to perform multiple sum queries on a subarray or need to calculate cumulative sums.'''
from typing import List
class Numarray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        curr = 0 

        for n in nums:
            curr = curr + n
            self.prefix.append(curr)

    def sumRange(self, left: int, right: int):
        rightSum = self.prefix[right]
        if left > 0:
           leftSum = self.prefix[left - 1]
        else:
           leftSum = 0
        return rightSum - leftSum
            
        
