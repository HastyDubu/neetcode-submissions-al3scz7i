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
                pv, pu = pu, pv
            
            rank[pu] += rank[pv]
            par[pv] = pu
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]          
            
            