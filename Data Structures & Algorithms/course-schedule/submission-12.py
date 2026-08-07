class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for src, dst in prerequisites:
            courses[src].append(dst)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if courses[crs] == []:
                return True
            
            visit.add(crs)
            for nei in courses[crs]:
                if not dfs(nei):
                    return False
            visit.remove(crs)
            courses[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True