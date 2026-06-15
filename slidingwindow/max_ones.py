#leetcode 1004 - Max Consecutive Ones III
class Solution(object):
    def longestOnes(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0 
        max_len = 0 
        count = 0

        for r in range(len(arr)):
            if arr[r] == 0:
                count+=1

            if count <=k :
                max_len = max(max_len, r - l + 1)
            else:
                if count > k:
                    if arr[l] == 0:
                        count-=1
                    l+=1

        return max_len