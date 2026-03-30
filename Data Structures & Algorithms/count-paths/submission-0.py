class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = [[-1] * n for _ in range(m)]

        def dfs(r, c):
            
            if r + 1 == m and c + 1 == n:
                return 1
            
            if (r >= m or c >= n):
                return 0
            
            if cache[r][c] != -1:
                return cache[r][c]
            
            cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            
            return cache[r][c]

        return dfs(0, 0)