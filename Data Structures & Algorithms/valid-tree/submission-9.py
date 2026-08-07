class DSU:
    def __init__(self, n):
        self.comp = n
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
        
        if pu < pv:
            pu, pv = pv, pu
        self.par[pv] = pu
        self.rank[pu] += self.rank[pv]
        self.comp -= 1
        return True

    def components(self):
        return self.comp

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)
        
        for src, dst in edges:
            if not dsu.union(src, dst):
                return False
        
        return dsu.components() == 1
        