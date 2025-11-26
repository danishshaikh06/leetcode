class Solution:
    def duplicate(self, arr):
        seen = set()
        duplicate = 0
        for i in arr:
            if i in seen:
                duplicate = i
            else:
                seen.add(i)
            
        return duplicate
    
sol = Solution()
arr = [2,2,2,2,2]
result = sol.duplicate(arr)
print(result)
