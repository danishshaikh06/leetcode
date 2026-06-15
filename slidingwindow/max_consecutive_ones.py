# Question : Max Consecutive Ones -> leetcode 485
#Given a binary array, find the maximum number of consecutive 1s in this array.
class Solution(object):
    def findMaxConsecutiveOnes(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = 0 
        max_len = 0 

        for r in range(len(arr)):
            if arr[r] == 0:
                l = r + 1
            max_len = max(max_len, r - l + 1)

        return max_len


        