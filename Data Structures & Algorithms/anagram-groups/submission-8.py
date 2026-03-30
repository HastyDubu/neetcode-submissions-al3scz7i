class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for w in strs:
            key = [0] * 26
            for c in w:
                key[ord(c) - ord("a")] += 1
            key = tuple(key)
            if key not in res:
                res[key] = []
            res[key].append(w)
        return [res[k] for k in res]