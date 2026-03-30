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
            rank[pu] += rank[pv]
            par[pv] = pu
            return True

        res = n
        for n1, n2 in edges:
            if union(n1, n2):
                res -= 1
        return res  