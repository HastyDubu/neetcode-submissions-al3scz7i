class DSU:
    
    def __init__(self, n):
        self.par = list(range(n + 1))
        self.rank = [1] * (n + 1)
        self.comps = n
    
    def find(self, node):
        if self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        
        self.comps -= 1
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu
        self.rank[pu] += self.rank[pv]
        self.par[pv] = pu
        return True

    def components(self):
        return self.comps

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)

        for n1, n2 in edges:
            if not dsu.union(n1, n2):
                return False
        return dsu.components() == 1