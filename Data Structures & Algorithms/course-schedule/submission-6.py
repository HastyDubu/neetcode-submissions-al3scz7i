class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        path = set()
        def dfs(src):
            if src in path:
                return False
            if not adj[src]:
                return True
            
            
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei):
                    return False
            path.remove(src)
            adj[src] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
        
