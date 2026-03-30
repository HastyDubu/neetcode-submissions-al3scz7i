class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        par = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(node):
            if par[node] != node:
                par[node] = find(par[node])
            return par[node]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            
            if pu == pv:
                return False
            
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu
            rank[pu] += rank[pv]
            par[pv] = pu
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]