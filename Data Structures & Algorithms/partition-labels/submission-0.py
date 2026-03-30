class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        res = []
        size = 0
        end = 0
        for i in range(len(s)):
            end = max(lastIndex[s[i]], end)
            size += 1
            if i == end:
                res.append(size)
                size = 0
        
        return res