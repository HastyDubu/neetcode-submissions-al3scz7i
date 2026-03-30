class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for w in strs:
            key = [0] * 26
            for c in w:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key not in dct:
                dct[key] = []
            dct[key].append(w)
        
        return [val for val in dct.values()]