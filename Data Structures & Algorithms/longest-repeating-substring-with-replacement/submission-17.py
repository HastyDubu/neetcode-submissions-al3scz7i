class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        l = 0
        counter = defaultdict(int)
        maxFreq = 0
        for r in range(len(s)):
            c = s[r]
            counter[c] += 1
            maxFreq = max(maxFreq, counter[c])
            while r - l  + 1 - maxFreq > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
