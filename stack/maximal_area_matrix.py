class Solution(object):
    def area_of_rec(self,arr):
        stack = []
        max_area = 0

        for i in range(len(arr)):
            while stack and arr[stack[-1]] >= arr[i]:
                element = arr[stack.pop()]
                nse = i

                if stack: # if len(stack) > 0:
                    pse = stack[-1]
                else:
                    pse = -1

                width = nse - pse - 1
                max_area = max(max_area, element * width)

            stack.append(i)

        while stack:
            element = arr[stack.pop()]
            nse = len(arr)

            if stack: # if len(stack) > 0:
                pse = stack[-1]
            else:
                pse = -1

            width = nse - pse - 1
            max_area = max(max_area, element * width)

        return max_area

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0 

        row = len(matrix)
        col = len(matrix[0])
        height = [0] * col
        max_area = 0 

        for i in range(row):
            for j in range (col):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0 

            max_area = max(max_area,self.area_of_rec(height))

        return max_area
        