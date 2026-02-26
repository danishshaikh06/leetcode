from typing import List
class Solution:
    def spiral_matrix(self ,mat):
        if not mat:
            return []
        
        n = len(mat)
        m = len(mat[0])
        top = 0
        bottom = n - 1
        left = 0
        right = m - 1
        result = []

        while(top <= bottom and left<= right):
            # top stays constant looping from left to right 
            for i in range (left, right + 1):
                result.append(mat[top][i])
            top+=1

            # right stays constant and we move top to bottom 
            for i in range(top, bottom  + 1):
                result.append(mat[i][right])
            right-=1
          
            if top<=bottom:
                # bottom stays constant and we move right to left
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom-=1

            if left<=right:
                # left stays constant move bottom to top
                for i in range(bottom , top - 1, -1):
                    result.append(mat[i][left])
                left+=1

        return result

           
sol = Solution()
m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
ans = sol.spiral_matrix(m)
print(ans)