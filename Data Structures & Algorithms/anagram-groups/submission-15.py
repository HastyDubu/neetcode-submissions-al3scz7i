class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for w in strs:
            key = [0] * 26
            for c in w:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)
            if key not in buckets:
                buckets[key] = []
            buckets[key].append(w)
        return [buckets[k] for k in buckets]