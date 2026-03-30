class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, last):
            
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or last >= matrix[r][c]):
                return 0
            
            res = 0
            res = 1 + max(
                res, 
                dfs(r + 1, c, matrix[r][c]),
                dfs(r - 1, c, matrix[r][c]), 
                dfs(r, c + 1, matrix[r][c]),
                dfs(r, c - 1, matrix[r][c]))
            return res
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c, float("-inf")))
        
        return res
