class DSU:
    def __init__(self, n):
        self.par = list(range(n + 1))
        self.rank = [1] * n
        self.comps = n
    
    def find(self, n):
        if self.par[n] != n:
            self.par[n] = self.find(self.par[n])
        return self.par[n]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu
        self.comps -=1
        self.par[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True
    
    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        return dsu.components() == 1