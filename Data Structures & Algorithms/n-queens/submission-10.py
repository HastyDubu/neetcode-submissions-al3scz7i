class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        posDiag, negDiag, col = set(), set(), set()

        def dfs(r):
            if r >= n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if (r + c) in posDiag or (r - c) in negDiag or c in col:
                    continue
                posDiag.add(r + c)
                negDiag.add(r - c)
                col.add(c)
                board[r][c] = "Q"
                dfs(r + 1)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                col.remove(c)
                board[r][c] = "."
            
            return
        
        dfs(0)
        return res
