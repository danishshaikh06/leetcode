class Solution(object):
    def print_subsets_unique(self, arr, ans, i, result):
        if i == len(arr):
            result.append(ans[:]) 
            return

        # Include arr[i]
        ans.append(arr[i])
        self.print_subsets_unique(arr, ans, i + 1, result)
        ans.pop()

        # Exclude arr[i]
        self.print_subsets_unique(arr, ans, i + 1, result)


    def subsetsWithDup(self, arr):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.print_subsets_unique(arr, [], 0, result)
        return result 