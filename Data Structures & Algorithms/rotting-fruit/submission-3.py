class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visit = set()
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    visit.add((r, c))
                    q.append((r, c))
        
        dist = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        time = 0
        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in dist:
                    row, col = r + dr, c + dc
                    if (min(row, col) < 0 or row >= ROWS or col >= COLS or (row, col) in visit or grid[row][col] == 0):
                        continue
                    visit.add((row, col))
                    fresh -= 1
                    grid[row][col] = 2
                    q.append((row, col))
            time += 1
        
        return time if fresh == 0 else -1