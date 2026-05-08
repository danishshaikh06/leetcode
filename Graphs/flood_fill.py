class Solution(object):
    def floodFill(self, image, i, j, new_col):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original = image[i][j]

        # if same color, no work needed
        if original == new_col:
            return image

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != original:
                return

            image[i][j] = new_col

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        dfs(i, j)
        return image