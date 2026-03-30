class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsDict = {}
        for w in strs:
            key = [0] * 26
            for c in w:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key not in strsDict:
                strsDict[key] = []
            strsDict[key].append(w)
        
        return [x for x in strsDict.values()]