class Solution(object):
    def totalFruit(self, arr):
        """
        :type fruits: List[int]
        :rtype: int
        """
        max_len = 0 
        l = 0 
        k = 2
        map = {}

        for r in range(len(arr)):
            map[arr[r]] = map.get(arr[r], 0) + 1

            while len(map) > k:
                map[arr[l]] -= 1
                if map[arr[l]] == 0:
                    del map[arr[l]] 
                l+=1

            if len(map) <= k:
                max_len = max(max_len, r - l + 1)

        return max_len