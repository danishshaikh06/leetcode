class Solution:
    def searchInRow(self,mat, target, row):
        start = 0
        end = len(mat[0]) - 1
        while (start <= end):
            mid = (start + end) // 2 
            if target == mat[row][mid]:
                return True
            elif target > mat[row][mid]:
                start = mid + 1
            else:
                end = mid - 1

        return False
    
    def search_target(self, mat, target: int):
        rows = len(mat)
        cols = len(mat[0])
        startRow = 0
        end = rows - 1
        while (startRow <= end ):
            mid = (startRow + end) // 2
            if (target >= mat[mid][0] and target<= mat[mid][cols - 1]):
                return self.searchInRow(mat, target, mid)
            elif target > mat[mid][cols- 1]:
                startRow = mid + 1
            else:
                end = mid - 1 
        return False

mat = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
sol = Solution()
print(sol.search_target(mat, 9))   # True
print(sol.search_target(mat, 10))  # False
