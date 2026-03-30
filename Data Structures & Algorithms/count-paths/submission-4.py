class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        ROWS, COLS = m, n
        dp = {}

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if (r, c) in dp:
                return dp[(r, c)]
            
            if min(r, c) < 0 or r >= ROWS or c >= COLS:
                return 0

            res = dfs(r + 1, c) + dfs(r, c + 1)
            dp[(r, c)] = res

            return res

        return dfs(0, 0)