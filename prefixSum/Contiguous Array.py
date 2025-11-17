from typing import List
class Sum:
    def Contiguous(self, nums: List[int]):
        hashmap = {}
        res = []
        for i , n in enumerate(nums):
            hashmap[i] = n
            