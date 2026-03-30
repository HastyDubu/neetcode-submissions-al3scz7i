class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for s in strs:
            w = [0] * 26
            for c in s:
                w[ord(c) - ord('a')] += 1
            w = tuple(w)
            if w not in res:
                res[w] = []
            res[w].append(s)
        
        return [item for item in res.values()]