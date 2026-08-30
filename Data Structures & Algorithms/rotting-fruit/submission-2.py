class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        row_count = len(grid)
        col_count = len(grid[0])
        minutes = 0
        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q:
            expanded = False
            size = len(q)
            for i in range(size):
                r, c = q.pop(0)  
                for rs, cs in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (r + rs < row_count and \
                        r + rs >= 0 and \
                        c + cs < col_count and \
                        c + cs >= 0 and \
                        grid[r + rs][c + cs] == 1):
                        expanded = True
                        q.append((r + rs, c + cs))
                        grid[r + rs][c + cs] = 2
            if expanded:
                minutes += 1

        for row in grid:
            if 1 in row:
                return -1
        return minutes
