class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = defaultdict(list)
        for src, dst in prerequisites:
            courses[src].append(dst)
        
        visit, cycle = set(), set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for nei in courses[crs]:
                if not dfs(nei):
                    return False
            visit.add(crs)
            cycle.remove(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
            