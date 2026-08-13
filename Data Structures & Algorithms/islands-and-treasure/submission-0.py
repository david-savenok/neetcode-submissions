class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = []
        row_count = len(grid)
        col_count = len(grid[0])
        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == 0:
                    queue.append((row, col))

        def bfs():
            while queue:
                row, col = queue.pop(0)
                for row_add, col_add in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if row + row_add < row_count and \
                       row + row_add >= 0 and \
                       col + col_add < col_count and \
                       col + col_add >= 0 and \
                       grid[row + row_add][col + col_add] > 0:
                        if 1 + grid[row][col] < grid[row + row_add][col + col_add]:
                            grid[row + row_add][col + col_add] = 1 + grid[row][col]
                            queue.append((row + row_add, col + col_add))
                    
        bfs()
                    