class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ROWS, COLS = m, n
        memo = {}

        def dfs(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            if min(r, c) < 0 or r >= ROWS or c >= COLS:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            res = dfs(r + 1, c) + dfs(r, c + 1)
            memo[(r, c)] = res
            return res

        return dfs(0, 0)
