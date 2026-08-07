class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

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
            
            par[pv] = pu
            rank[pu] += rank[pv]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            