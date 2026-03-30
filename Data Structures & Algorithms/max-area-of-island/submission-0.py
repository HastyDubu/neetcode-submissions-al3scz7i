class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        area = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):

            if (min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0):
                return 0
             
            visited.add((r,c))

            return 1 + (dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c  + 1) + dfs(r, c  - 1))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        
        return area