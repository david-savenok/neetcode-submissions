class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.seen = [[False] * self.cols for i in range(self.rows)]
        self.max_area = 0

        def dfs(row, col):
            self.seen[row][col] = True
            size = 0
            if row + 1 < self.rows and not self.seen[row + 1][col] and grid[row + 1][col] == 1:
                size += 1 + dfs(row + 1, col)
            if row - 1 >= 0 and not self.seen[row - 1][col] and grid[row - 1][col] == 1:
                size += 1 + dfs(row - 1, col)
            if col + 1 < self.cols and not self.seen[row][col + 1] and grid[row][col + 1] == 1:
                size += 1 + dfs(row, col + 1)
            if col - 1 >= 0 and not self.seen[row][col - 1] and grid[row][col - 1] == 1:
                size += 1 + dfs(row, col - 1)
            return size
        
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1 and not self.seen[row][col]:
                    self.max_area = max(self.max_area, 1 + dfs(row, col))
        
        return self.max_area