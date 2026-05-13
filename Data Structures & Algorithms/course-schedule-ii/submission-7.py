class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, pre in prerequisites:
            adj[src].append(pre)
        
        visit, cycle = set(), set()
        output = []
        def dfs(src):
            if src in cycle:
                return False
            if src in visit:
                return True
            
            cycle.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            cycle.remove(src)
            visit.add(src)
            output.append(src)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output