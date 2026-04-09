class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = list(range(n))
        rank = [1] * n

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
        
        res = n
        for u, v in edges:
            if union(u, v):
                res -= 1
        return res
        
        