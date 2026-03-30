class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            
            return res
        
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