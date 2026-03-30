class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        for src, dst in prerequisites:
            preMap[src].append(dst)
        
        path = set()

        def dfs(src):
            if src in path:
                return False

            if preMap[src] == []:
                return True

            path.add(src)
            for dst in preMap[src]:
                if not dfs(dst):
                    return False
            path.remove(src)
            preMap[src] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
