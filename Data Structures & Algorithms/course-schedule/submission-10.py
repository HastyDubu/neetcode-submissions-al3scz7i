class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)
        for src, pre in prerequisites:
            courses[src].append(pre)
        visit = set()

        def dfs(src):
            if src in visit:
                return False
            if courses[src] == []:
                return True

            visit.add(src)
            for nei in courses[src]:
                if not dfs(nei):
                    return False
            visit.remove(src)
            courses[src] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
