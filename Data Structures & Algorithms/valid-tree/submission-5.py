class DSU:

    def __init__(self, n):
        self.par = list(range(n + 1))
        self.rank = [1] * (n + 1)
        self.components = n

    def find(self, root):
        if self.par[root] != root:
            self.par[root] = self.find(self.par[root])
        return self.par[root]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False
        
        self.components -= 1
        if self.rank[pu] < self.rank[pv]:
            pu, pv = pv, pu
        self.rank[pu] += self.rank[pv]
        self.par[pv] = pu
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v):
                return False
        
        return dsu.components == 1