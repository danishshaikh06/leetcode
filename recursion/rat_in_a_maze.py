class Solution:

    def solvemaze(self, maze, r, c, ans, path):

        # Boundary + blocked + visited check
        if (r < 0 or c < 0 or 
            r >= len(maze) or c >= len(maze) or 
            maze[r][c] == 0 or maze[r][c] == -1):
            return

        # If destination reached
        if r == len(maze) - 1 and c == len(maze) - 1:
            ans.append(path)
            return

        # Mark as visited
        maze[r][c] = -1

        # Move in 4 directions
        self.solvemaze(maze, r+1, c, ans, path + 'D')
        self.solvemaze(maze, r-1, c, ans, path + 'U')
        self.solvemaze(maze, r, c+1, ans, path + 'R')
        self.solvemaze(maze, r, c-1, ans, path + 'L')

        # Backtrack (unvisit)
        maze[r][c] = 1


    def findPath(self, maze):
        ans = []
        self.solvemaze(maze, 0, 0, ans, "")
        return ans

# Example maze
maze = [
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 1]
]

solver = Solution()
paths = solver.findPath(maze)
print("All possible paths from start to destination:")
print(paths) 