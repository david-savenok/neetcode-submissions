class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        seen = [[False] * len(grid[0]) for i in range(len(grid))]

        def dfs(grid, i, j):
            seen[i][j] = True
            if i + 1 < len(grid) and not seen[i + 1][j] and grid[i + 1][j] == "1":
                dfs(grid, i + 1, j)
            if i - 1 >= 0 and not seen[i - 1][j] and grid[i - 1][j] == "1":
                dfs(grid, i - 1, j)
            if j + 1 < len(grid[0]) and not seen[i][j + 1] and grid[i][j + 1] == "1":
                dfs(grid, i, j + 1)
            if j - 1 >= 0 and not seen[i][j - 1] and grid[i][j - 1] == "1":
                dfs(grid, i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if seen[i][j] or grid[i][j] == "0":
                    continue
                count += 1
                dfs(grid, i, j)

        return count
        