class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(j, i):
            if i >= len(s):
                if i == j:
                    res.append(path.copy())
                return

            if self.isPali(s, j, i):
                path.append(s[j: i + 1])
                dfs(i + 1, i + 1)
                path.pop()
            
            dfs(j, i + 1)
        
        dfs(0, 0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True    
            