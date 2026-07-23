class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for i in range(9)]
        rows = [set() for i in range(9)]
        sqrs = [set() for i in range(9)]

        num_rows = len(board)
        num_cols = len(board[0])

        for i in range(num_rows):
            for j in range(num_cols):
                if not board[i][j].isdigit():
                    continue
                idx = (i // 3) * 3 + (j // 3)
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in sqrs[idx]:
                    print(i, j, idx, board[i][j])
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                sqrs[idx].add(board[i][j])
        return True