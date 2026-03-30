class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for w in strs:
            key = [0] * 26
            for c in w:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key not in count:
                count[key] = []
            count[key].append(w)
        return [count[k] for k in count]