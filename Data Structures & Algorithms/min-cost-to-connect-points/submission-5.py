class DSU:
    def __init__(self, n):
        self.par = list(range(n + 1))
        self.rank = [1] * (n + 1)

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
        edges = []
        n = len(points)
        dsu = DSU(n)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append([dist, i, j])
        
        edges.sort()
        res = 0 
        for dst, i, j in edges:
            if dsu.union(i, j):
                res += dst
        return res
