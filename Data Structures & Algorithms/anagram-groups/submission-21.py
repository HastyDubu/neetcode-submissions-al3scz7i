class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for w in strs:
            key = [0] * 26
            for c in w:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            res[key].append(w)
        
        return [item for item in res.values()]