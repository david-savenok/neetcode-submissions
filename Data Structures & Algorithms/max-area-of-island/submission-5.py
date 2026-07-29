class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.seen = [[False] * self.cols for i in range(self.rows)]
        self.max_area = 0

        def dfs(row, col):
            if row < 0 or row == self.rows or col < 0 or col == self.cols or self.seen[row][col] or grid[row][col] == 0:
                return 0
            self.seen[row][col] = True

            return (1 + dfs(row + 1, col) +
                        dfs(row - 1, col) +
                        dfs(row, col + 1) +
                        dfs(row, col - 1))
        
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1 and not self.seen[row][col]:
                    self.max_area = max(self.max_area, dfs(row, col))
        
        return self.max_area