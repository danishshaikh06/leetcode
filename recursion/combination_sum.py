class Solution(object):
    def helper(self, arr, current, target, ans, start):
        # Base case: valid combination
        if target == 0:
            ans.append(list(current))
            return
        
        # Base case: target overshot
        if target < 0:
            return
        
        # Try numbers starting from 'start' to allow reuse
        for i in range(start, len(arr)):
            current.append(arr[i])
            self.helper(arr, current, target - arr[i], ans, i)  # i = reuse same number
            current.pop()  # backtrack

    def combinationSum(self,arr, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        self.helper(arr, [], target, ans, 0)
        return ans