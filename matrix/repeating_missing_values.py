class solution:
    def count_duplicates_and_missing(self, grid):
        n = len(grid)             # grid is n x n
        size = n * n              # numbers go from 1 to n^2
        seen = set()
        duplicate = -1

        # Flatten and detect duplicate
        for row in grid:
            for num in row:
                if num in seen:
                    duplicate = num
                else:
                    seen.add(num)

        # Expected set of all numbers
        expected = set(range(1, size + 1))

        # Missing = expected - seen
        missing = list(expected - seen)[0]

        return duplicate, missing


sol = solution()
grid = [
  [1,2],
  [2,4]
]
result = sol.count_duplicates_and_missing(grid)
print(list(result))



  

