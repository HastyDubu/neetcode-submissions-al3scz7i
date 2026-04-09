class DSU:

    def __init__(self, n):
        self.par = list(range(n + 1))
        self.rank = [1] * n
    
    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        
        if pu == pv:
            return False
        
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu
        self.par[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)
        edges = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        
        res = 0
        edges.sort()
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        
        return res